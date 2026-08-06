import os
import time

from dotenv import load_dotenv
from google import genai

from app.core.logger import logger


# Load environment variables
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to the .env file."
    )


class GeminiLLM:
    """
    Gemini Large Language Model client.
    """

    def __init__(self):
        logger.info("Initializing Gemini...")

        self.client = genai.Client(api_key=API_KEY)

        self.model_name = "gemini-3.6-flash"

        logger.info(
            f"Gemini initialized successfully using {self.model_name}."
        )

    def generate(self, prompt: str) -> str:
        """
        Generate an answer using Gemini.
        """

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        logger.info("Sending prompt to Gemini...")

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = self.client.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                )

                logger.info("Response received from Gemini.")

                if not response.text:
                    return "I couldn't generate a response."

                return response.text.strip()

            except Exception as error:

                logger.error(
                    f"Gemini API Error (Attempt {attempt + 1}/{max_retries}): {error}"
                )

                if attempt < max_retries - 1:
                    logger.info("Retrying in 2 seconds...")
                    time.sleep(2)
                    continue

                error_text = str(error)

                if "503" in error_text or "UNAVAILABLE" in error_text:
                    return (
                        "The AI service is temporarily unavailable due to high demand. "
                        "Please try again in a few moments."
                    )

                if "429" in error_text:
                    return (
                        "The AI service rate limit has been reached. "
                        "Please wait a minute and try again."
                    )

                return (
                    "An unexpected error occurred while generating the response. "
                    "Please try again later."
                )