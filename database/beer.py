from typing import List
from database.models import Beer
from bson.objectid import ObjectId
from database.connection import db

class BeerService:
    # MongoDB에 있는 'Beers'라는 이름의 컬렉션을 참조하도록 설정합니다.
    collection = db['Beers']

    @classmethod
    async def create(cls, beer: Beer) -> Beer:
        # Beer 객체를 dictionary 형태로 변환합니다.
        beer_dict = beer.dict()

        # MongoDB에서는 "_id"라는 필드를 사용하여 고유한 ID를 관리합니다.
        # 이를 위해 ObjectId를 생성하여 "_id" 필드에 할당합니다.
        beer_dict["_id"] = ObjectId()

        # 생성된 Beer 객체를 'beers' 컬렉션에 삽입합니다.
        await cls.collection.insert_one(beer_dict)

        # 생성된 Beer 객체를 반환합니다.
        return beer

    @classmethod
    async def read(cls, beer_id: str) -> Beer:
        # 주어진 ID를 가진 Beer를 'beers' 컬렉션에서 찾습니다.
        # 여기서 ID는 ObjectId 형태이므로 str 형태의 beer_id를 ObjectId로 변환합니다.
        beer = await cls.collection.find_one({"beer_id": ObjectId(beer_id)})

        # 찾은 Beer를 Beer 객체로 변환하여 반환하거나, 찾지 못한 경우 None을 반환합니다.
        return Beer(**beer) if beer else None
    
    # BeerService in beer.py
    @classmethod
    async def read_by_name(cls, beer_name: str) -> Beer:
        beer = await cls.collection.find_one({"name": beer_name})
        return Beer(**beer) if beer else None

    @classmethod
    async def read_all(cls) -> List[Beer]:
        # 'beers' 컬렉션의 모든 Beer를 찾습니다. 
        # 이 예제에서는 최대 100개의 Beer를 반환하도록 설정하였습니다.
        beers = await cls.collection.find().to_list(length=100)

        # 찾은 모든 Beer를 Beer 객체로 변환하여 리스트 형태로 반환합니다.
        return [Beer(**beer) for beer in beers]

    @classmethod
    async def update(cls, beer_id: str, beer: Beer) -> Beer:
        # 주어진 ID를 가진 Beer를 새로운 Beer로 업데이트합니다.
        # 이때 ID는 ObjectId 형태이므로 str 형태의 beer_id를 ObjectId로 변환합니다.
        await cls.collection.replace_one({"beer_id": ObjectId(beer_id)}, beer.dict())

        # 업데이트된 Beer를 반환합니다.
        return await cls.read(beer_id)

    @classmethod
    async def delete(cls, beer_id: str) -> None:
        # 주어진 ID를 가진 Beer를 'beers' 컬렉션에서 삭제합니다.
        await cls.collection.delete_one({"beer_id": ObjectId(beer_id)})
