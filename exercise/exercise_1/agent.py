# Create PydanticAI agent

# This is where your LLM logic lives.
from constants import MODEL_LARGE
from pydantic_ai import Agent
from models import Restaurant
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model=MODEL_LARGE,
    system_prompt="""
You are a restaurant recommendation assistant.

Given a location and cuisine, generate ONE realistic restaurant.

Return:
- name
- cuisine
- price_level ($, $$, $$$)
- rating (0-5)
- description
- opening_hours
- location

Be realistic and concise.
""", output_type=Restaurant
)

def generate_restaurant(location: str, cuisine: str) -> Restaurant:
    prompt = (
        f"Create one realistic restaurant for this request.\n"
        f"Location: {location}\n"
        f"cuisine{cuisine}"
    )
    result = agent.run_sync(prompt)
    return result.output