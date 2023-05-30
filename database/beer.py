from typing import List
from database.models import Beer
from bson.objectid import ObjectId
from database.connection import db

class BeerService:
    collection = db['Beers']

    @classmethod
    async def create(cls, beer: Beer) -> Beer:
        beer_dict = beer.dict()
        beer_dict["_id"] = ObjectId()
        await cls.collection.insert_one(beer_dict)
        return beer

    @classmethod
    async def read(cls, beer_id: str) -> Beer:
        beer = await cls.collection.find_one({"beer_id": beer_id})
        return Beer(**beer) if beer else None
    
    @classmethod
    async def read_by_name(cls, beer_name: str) -> Beer:
        beer = await cls.collection.find_one({"name": beer_name})
        return Beer(**beer) if beer else None

    @classmethod
    async def read_all(cls) -> List[Beer]:
        beers = await cls.collection.find().to_list(length=100)
        return [Beer(**beer) for beer in beers]

    @classmethod
    async def update(cls, beer_id: str, beer: Beer) -> Beer:
        await cls.collection.replace_one({"beer_id": beer_id}, beer.dict())
        return await cls.read(beer_id)

    @classmethod
    async def delete(cls, beer_id: str) -> None:
        await cls.collection.delete_one({"beer_id": beer_id})
