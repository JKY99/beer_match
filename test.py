from database.database import *
from database.models import *
import asyncio

import random
import string
from database.connection import db

def get_random_id(length: int = 10) -> str:
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# MongoDB에 연결합니다.
collection = db.Beers

async def rearrange_fields(collection):
    async for beer in collection.find():
        new_beer = {
            'beer_id': beer['beer_id'],
            'name': beer['name'],
            'origin': beer['origin'],
            'category': beer['category'],
            'sweetness': beer['sweetness'],
            'bitterness': beer['bitterness'],
            'sourness': beer['sourness'],
            'ABV': beer['ABV'],
            'food_pairing': beer['food_pairing'],
            'taste': beer['taste'],
            'image_path': beer['image_path'],
            'rating': beer['rating']
        }
        await collection.replace_one({'_id': beer['_id']}, new_beer)

# asyncio.run(rearrange_fields(collection))
