# Pydantic model/schemas

from pydantic import BaseModel, Field
from typing import Literal 

class RestaurantSearcher(BaseModel):
    name: str = Field(description="Restaurant name")
    type_of_food: str = Field(description="Type of food or cuisine")
    price_level: Literal["$","$$","$$$"] = Field(description="Approxiately price range")
    rating: Literal["1","2","3","4","5"] 
    short_description: str = Field(description="Short summary about the type of cusinie the Restaurant offers")
    opening_hours: float = Field(descrioption="Opening hours as text")
    location: str = Field(description="Restaruant location/address/area")

class RestaurantList(BaseModel):
    restaurants: list[RestaurantSearcher] = Field(
        min_length=5,
        max_length=5,
        description="Exactly 5 restaurant suggestions"
    )