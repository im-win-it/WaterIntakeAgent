from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-oss-20b:free"
)

class WaterIntakeAgent:
    def __init__(self):
        self.history = []

    def analyze_intake(self, intake_ml):
        prompt = f"""
        You are a hydration agent. The person has drunk {intake_ml} millilitres of water so far.
        Tell their hydration status. Do they need to drink more water?
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content


# Example usage
#agent = WaterIntakeAgent()
#print(agent.analyze_intake(1200))
