# Define Pydantic model/schemas

from pydantic import BaseModel, Field

class Restaurant(BaseModel):
    name: str
    cuisine: str
    price_level: str = Field(description="e.g. $, $$, $$$")
    rating: float
    short_description: str
    opening_hours: str
    location: str


class RestaurantRequest(BaseModel):
    location: str
    cuisine: str

class RestaurantResponse(BaseModel):
    message: str
    restaurant: Restaurant

class RestaurantRow(Restaurant):
    id: int