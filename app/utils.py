# utils.py
import os
from fastapi import HTTPException
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from a .env file (useful for local development)
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_env_variable(key: str, default: Optional[str] = None) -> str:
    """
    Fetch an environment variable with a fallback to a default value.
    Raises an HTTPException if the variable is not found and no default is provided.
    """
    value = os.getenv(key, default)
    if value is None:
        logger.error(f"Environment variable '{key}' is not set and no default value provided.")
        raise HTTPException(status_code=500, detail=f"Missing required environment variable: {key}")
    return value

def format_response(success: bool, message: str, data: Optional[dict] = None) -> dict:
    """
    Format a consistent response structure for API endpoints.
    """
    return {
        "success": success,
        "message": message,
        "data": data or {}
    }

def log_exception(error: Exception):
    """
    Log an exception with a consistent format.
    """
    logger.error(f"An error occurred: {str(error)}", exc_info=True)

# Example utility for validating input
def validate_input_length(value: str, min_length: int, max_length: int):
    """
    Validate the length of a string input.
    Raises an HTTPException if the input does not meet length requirements.
    """
    if not (min_length <= len(value) <= max_length):
        raise HTTPException(
            status_code=400,
            detail=f"Input must be between {min_length} and {max_length} characters."
        )
