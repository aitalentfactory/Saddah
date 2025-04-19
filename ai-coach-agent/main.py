import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from starlette.middleware.cors import CORSMiddleware

from src.controller.Coach_Controller import aiCoach
from src.controller.User_Controller import aiUser

load_dotenv()
LLM_TRAINED_MODEL = os.getenv("LLM_TRAINED_MODEL", "tinyllama")
LLM_RANKED_MODEL = os.getenv("LLM_RANKED_MODEL", "tinyllama")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "tinyllama")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.llm_trained_model = ChatOpenAI(
                model=LLM_TRAINED_MODEL,
                openai_api_key=OPENAI_API_KEY
            )
    app.state.llm_rank_model = ChatOpenAI(
        model=LLM_RANKED_MODEL,
        openai_api_key=OPENAI_API_KEY
    )
    print("🚀 LLM Model Loaded!")
    yield
    print("🛑 Shutting down LLM Model...")  # Cleanup if needed
    del app.state.llm_trained_model  # Free resources
    del app.state.llm_rank_model  # Free resources
app = FastAPI(lifespan=lifespan)

app.include_router(aiCoach)
app.include_router(aiUser)
# Add CORSMiddleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List of allowed origins
    allow_credentials=False,
    allow_methods=["*"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allowed headers
)