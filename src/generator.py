import google.generativeai as genai
import os
from typing import List
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

class Generator:
    """
    Generates an answer using a language model based on retrieved context and a query.
    """
    def __init__(self):
        """
        Initializes the Generator with the Gemini model.
        """
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel('gemini-2.0-flash')

    def generate_answer(self, query: str, contexts: List[str]) -> str:
        """
        Generates an answer based on the provided query and context.

        Args:
            query (str): The user query.
            contexts (List[str]): A list of relevant text chunks (context).

        Returns:
            str: The generated answer.
        """
        context_text = "\n\n".join(contexts)

        prompt = f"""
        You are a helpful assistant. Use the following information to answer the question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context:
        {context_text}

        Question:
        {query}

        Answer:
        """

        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating answer: {e}")
            return "Could not generate an answer."

if __name__ == '__main__':
    # Example usage (for testing)
    sample_contexts = [
        "Cats are domesticated carnivorous mammals.",
        "They are known for their agility and hunting skills."
    ]
    sample_query = "What are cats?"

    generator = Generator()
    answer = generator.generate_answer(sample_query, sample_contexts)
    print(f"Answer: {answer}")
