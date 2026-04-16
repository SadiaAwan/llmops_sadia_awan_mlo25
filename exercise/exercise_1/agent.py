# PydanticAI agent

# Create Agent

# This is where your LLM logic lives.

from pydantic import BaseModel, Field
from models import RestaurantList
from pydantic_ai import Agent



agent = Agent(
    "openrouter:nvidia/nemotron-3-super-120b-a12b:free",
    system_prompt=""" 
You are a restaurant recommendation assistant.
The user gives you a location.
Return exactly 5 restaurant near the place.
It is allowed to invent restaurant if needed, 
but they should still look realistic and relevant to the location.
Very cuisine types.
Keep descriptions short and useful.
Ratings must be between 1 and 5.
Price level must be one of: $, $$, $$$

    """, output_type=RestaurantList)


async def generate_restaurant(location: str, cuisine: str):
    prompt = f"Location: {location}, Cuisine: {cuisine}"
    result = await agent.run(prompt)
    return result.data