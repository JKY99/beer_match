from typing import List
from database.models import Beer
from database.connection import db

# Beer에 대한 CRUD 연산을 수행하는 BeerService 클래스입니다.
class BeerService:
    collection = db['Beers']

    @classmethod
    async def get_best_beers(cls) -> List[Beer]:
        # 맥주를 알코올 도수(ABV)가 높은 순으로 정렬하고, 상위 5개만 선택
        best_beers = await cls.collection.find().sort('ABV', -1).limit(5).to_list(length=100)
        return [Beer(**beer) for beer in best_beers]

    @classmethod
    async def get_beginner_beers(cls) -> List[Beer]:
        # 맥주를 알코올 도수(ABV)가 낮은 순으로 정렬하고, 상위 5개만 선택
        beginner_beers = await cls.collection.find().sort('ABV', 1).limit(5).to_list(length=100)
        return [Beer(**beer) for beer in beginner_beers]
