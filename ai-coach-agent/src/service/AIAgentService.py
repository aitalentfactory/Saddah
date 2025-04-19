import json

from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END
from sqlalchemy.orm import Session

from src.dto.TrainingDTO import TrainingDTO
from src.dto.UserWrapperDTO import UserWrapperDTO
from src.mapper.UserMapper import userWrapperDTO_to_dict, userDTOs_to_users, users_to_userResponseDTOs
from src.service.PromptService import generate_report_prompt, generate_training_prompt, generate_prompt_routh, \
    extract_name, prompt_translation, generate_rank_prompt
from src.service.PlayerMetricService import PlayerMetricService
from src.service.TrainingService import TrainingService
from src.service.UserService import UserService
from src.util.CommonUtil import get_score


class AIAgentService:
    def __init__(self,llm_trained_model,llm_rank_model,db: Session):
        self.userService = UserService(db)
        self.playerMetricService = PlayerMetricService(db)
        self.trainingService = TrainingService(db)
        self.llm_trained_model = llm_trained_model
        self.llm_rank_model = llm_rank_model

        workflow = StateGraph(dict)
        workflow.add_node("translation", self.translation_node)
        workflow.add_node("supervisor", self.supervisor_node)
        workflow.add_node("report_agent", self.report_agent_node)
        workflow.add_node("trainer_agent", self.trainer_agent_node)
        workflow.add_node("ai_agent", self.ai_agent_node)
        # Configure edges
        workflow.add_edge(START, "translation")

        workflow.add_edge("translation", "supervisor")
        # Conditional routing from supervisor
        workflow.add_conditional_edges(
            "supervisor",
            lambda state: state["last_routed"],  # Route based on the supervisor's decision
            {
                "report_agent": "report_agent",
                "ai_agent": "ai_agent",
            },
        )

        workflow.add_edge("report_agent", "trainer_agent")


        # RAG agent direct path
        workflow.add_edge("trainer_agent", END)  # Explicit edge to END
        workflow.add_edge("ai_agent", END)  # Explicit edge to END

        workflow.set_entry_point("translation")

        self.compiled_graph = workflow.compile()

    def invoke(self,initial_state):
        try:
            result = self.compiled_graph.invoke(initial_state)
            print(f"Init result: {result}")
            final_state = result.get("update", {})
            return result
        except Exception as e:
            print(f"Graph execution error: {str(e)}")
            return "System error occurred"

    def supervisor_node(self, state: dict) -> dict:
        # Preserve all existing state
        new_state = state.copy()
        question = new_state.get("question", "").strip()
        gptMode = new_state.get("gpt_mode", "").strip()

        prompt = generate_prompt_routh(question)
        answer = self.llm_trained_generate(prompt)

        print(f"inside supervisor_node gptMode: {answer}")

        if answer == 'KB':
            new_state["last_routed"] = "report_agent"
        elif answer == 'RK':
            new_state["last_routed"] = "rank_agent"
        else:
            new_state["last_routed"] = "ai_agent"

        print(f"[Supervisor] Routing to: {new_state['last_routed']}")
        return new_state

    def report_agent_node(self,state: dict) -> dict:
        # Safely extract question with fallback
        question = state.get("question", "No question provided")
        print(f"inside report_agent_node question: {question}")

        try:
            # Generate answer
            prompt = extract_name(question)
            name = self.llm_trained_generate(prompt)
            print(f"inside report_agent_node name: {name}")
            userDTO = self.userService.get_user_by_name(name)
            playerMetricDTOs = self.playerMetricService.get_latest_10_player_metrics_by_user_uuid(userDTO.uuid)
            playerMetricsJson = self.playerMetricService.convert_player_list_metric_to_json(playerMetricDTOs)

            prompt = generate_report_prompt(playerMetricsJson)
            answer = self.llm_trained_generate(prompt)
            #print(f"[Report Agent] Generated answer: {answer}")

            state.update({"user_uuid": userDTO.uuid, "report_result": answer,"player_name": name})
            return state
        except Exception as e:
            print(f"[Report Agent] Error: {str(e)}")
            state.update({"final_answer": str(e)})
            return state

    def trainer_agent_node(self,state: dict) -> dict:
        # Safely extract question with fallback
        print(f"inside trainer_agent_node")
        question = state.get("question")
        report = state.get("report_result", "No report provided")
        user_uuid = state.get("user_uuid")
        try:
            # Generate answer
            trainingDTOs = self.trainingService.get_latest_training_by_userUuid(user_uuid)
            trainingDTOJson = self.trainingService.convert_trainingDTO_list_to_json(trainingDTOs)

            prompt = generate_training_prompt(trainingDTOJson,report,question)
            answer = self.llm_trained_generate(prompt)

            trainingDTO = TrainingDTO()
            trainingDTO.training = answer
            trainingDTO.user_uuid = user_uuid

            self.trainingService.save_training(trainingDTO)

            print(f"[Trainer Agent] Generated answer: {answer}")

            state.update({"final_answer": answer})
            return state
        except Exception as e:
            print(f"[Trainer Agent] Error: {str(e)}")
            state.update({"final_answer": str(e)})
            return state

    def ai_agent_node(self, state: dict) -> dict:
        # Safely extract question with fallback
        print(f"inside ai_agent_node")
        question = state.get("question", "No question provided")

        try:
            # Generate answer
            prompt = f"""
            You are a helpful AI assistant. Answer the following question: {question}
            """
            answer = self.llm_trained_generate(prompt)
            print(f"[AI Agent] Generated answer: {answer}")

            state.update({"final_answer": answer})
            return state
        except Exception as e:
            print(f"[AI Agent] Error: {str(e)}")
            state.update({"final_answer": str(e)})
            return state

    def translation_node(self, state: dict) -> dict:
        question = state.get("question", "")
        print(f"Original Question: {question}")

        try:
            prompt = prompt_translation(question)
            translated = self.llm_trained_generate(prompt)
            print(f"[Translation Node] Translated Question: {translated}")
            state["question"] = question
        except Exception as e:
            print(f"[Translation Node] Error: {str(e)}")
            state["translation_error"] = str(e)

        return state

    def llm_trained_generate(self, prompt: str) -> str:
        """Function to send requests to OpenAI's GPT model."""

        # Prepare the message list with a single human message
        messages = [HumanMessage(content=prompt)]

        # Invoke the model with the structured message format
        response = self.llm_trained_model.invoke(messages)

        # Return the response as a string
        return response.content

    def llm_rank_generate(self, prompt: str) -> str:
        """Function to send requests to OpenAI's GPT model."""

        # Prepare the message list with a single human message
        messages = [HumanMessage(content=prompt)]

        # Invoke the model with the structured message format
        response = self.llm_rank_model.invoke(messages)

        # Return the response as a string
        return response.content


    def get_users_with_score_evaluation(self):
        userDTOs = self.userService.get_users_dtos()

        userWrapperDTOs = []
        for user in userDTOs:
            userWrapperDTO = UserWrapperDTO()
            userWrapperDTO.user = user
            userWrapperDTO.playerMetrics = self.playerMetricService.get_latest_3_player_metrics_by_user_uuid(user.uuid)
            userWrapperDTO.trainings = self.trainingService.get_latest_3_training_by_userUuid(user.uuid)
            userWrapperDTOs.append(userWrapperDTO)


        jsonDict = userWrapperDTO_to_dict(userWrapperDTOs)

        prompt = generate_rank_prompt(jsonDict)
        response = self.llm_rank_generate(prompt)

        users = userDTOs_to_users(userDTOs)
        userResponseDTOs = users_to_userResponseDTOs(users)
        userResponseDTOs = self.score_users(userResponseDTOs,response)
        return userResponseDTOs

    def score_users(self, userResponseDTOs, aiResponse):
        # Create a map from user_uuid to rank from the AI response (dict-based)
        aiResponseDict = json.loads(aiResponse)
        uuid_to_rank = {user["uuid"]: user["rank"] for user in aiResponseDict["users"]}

        # Map rank to each userResponseDTO by uuid
        for userResponseDTO in userResponseDTOs:
            if userResponseDTO.uuid in uuid_to_rank:
                userResponseDTO.rank = uuid_to_rank[userResponseDTO.uuid]
            else:
                userResponseDTO.rank = None  # Or a default/fallback rank

        return userResponseDTOs