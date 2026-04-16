# Keep DB logic separate — this is good MLOps hygiene

import duckdb
from models import RestaurantSearcher

DB_FILE = "restaurants.db"

def init_db():
    conn = duckdb.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS restaurants (
            name TEXT,
            cuisine TEXT,
            price_level TEXT,
            rating DOUBLE,
            description TEXT,
            opening_hours TEXT,
            location TEXT
        )
    """)
    conn.close()


def insert_restaurant(r: RestaurantSearcher):
    conn = duckdb.connect(DB_FILE)
    conn.execute("""
        INSERT INTO restaurants VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        r.name,
        r.cuisine,
        r.price_level,
        r.rating,
        r.description,
        r.opening_hours,
        r.location
    ))
    conn.close()


def get_all_restaurants():
    conn = duckdb.connect(DB_FILE)
    rows = conn.execute("SELECT * FROM restaurants").fetchall()
    conn.close()
    return rows