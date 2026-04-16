# FastAPI app

# Now you expose everything

from contextlib import asynccontextmanager
from fastapi import FastAPI
from models import RestaurantRequest, RestaurantResponse, RestaurantRow
from agent import generate_restaurant
from db import init_db, insert_restaurant, get_all_restaurants


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def root():
    return{"message": "Restaurant Generator API is running"}


@app.post("/restaurants/generate", response_model=RestaurantResponse)
def create_restaurant(request: RestaurantRequest):
    restaurant = generate_restaurant(
        location=request.location,
        cuisine=request.cuisine
    )

    insert_restaurant(restaurant)

    return RestaurantResponse(
        message="Restaurant created",
        restaurant=restaurant,
    )

@app.get("/restaurants", response_model=list[RestaurantRow])
def list_restaurants():
    restaurants = get_all_restaurants()
    return {"restaurants": restaurants}