import logging

logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format="%(asctime)s - %(message)s",  # Define the log message format
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()         # Log to the console
    ]
)
logger = logging.getLogger("ai-coach-agent")  # Create a logger instance