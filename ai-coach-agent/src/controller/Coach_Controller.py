from typing import List

from fastapi import APIRouter, Depends
from src.configuration.Dependencies import get_ai_agent_service, get_user_service
from src.requestDTO.AgentStateRequestDTO import AgentStateRequestDTO
from src.responseDTO.AgentResponseDTO import AgentResponseDTO
from src.responseDTO.UserResponseDTO import UserResponseDTO
from src.service.AIAgentService import AIAgentService
from src.service.UserService import UserService

aiCoach = APIRouter()


@aiCoach.post("/coach", response_model=AgentResponseDTO ,tags=["AI Coach"])
async def coach(agentStateRequestDTO: AgentStateRequestDTO,
                        aiAgentService: AIAgentService = Depends(get_ai_agent_service)  # Use the singleton
                        ) -> AgentResponseDTO:
        #logger.info(f"Coach Controller coach: {agentStateRequestDTO}")

        initial_state = agentStateRequestDTO.dict()
        question = agentStateRequestDTO.message.strip()
        gptMode = agentStateRequestDTO.gpt_mode.strip()
        initial_state.update({
            "question": question,
            "schema_info": None,
            "attempts": 0,
            "last_routed": None,
            "validation_errors": None,
            "report_result": None,
            "final_answer": None,
            "gpt_mode": gptMode,
            "user_uuid": None,
            "player_name": None
        })
        agentResponseDTO = AgentResponseDTO()
        result = aiAgentService.invoke(initial_state)
        agentResponseDTO.response = result.get("final_answer")
        agentResponseDTO.playerReport = result.get("report_result")
        agentResponseDTO.playerName = result.get("player_name")
        return agentResponseDTO


@aiCoach.get("/players_evaluation", response_model=List[UserResponseDTO] ,tags=["Get All Players Evaluations"])
async def players_evaluation(aiAgentService: AIAgentService = Depends(get_ai_agent_service) # Use the singleton
                        ) -> List[UserResponseDTO]:

    return aiAgentService.get_users_with_score_evaluation()