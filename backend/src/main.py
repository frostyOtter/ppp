from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
import sys

# Configure logging
logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("logs/app.log", rotation="500 MB", level="INFO")

app = FastAPI(title="PDF Parser API")

# Configure CORS
origins = [
    "http://localhost:5173",
    # Add other origins if needed, e.g., "*" for development
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to PDF Parser API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}