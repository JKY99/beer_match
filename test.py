from database.database import *
from database.models import *
import asyncio

from typing import List
import random
import string
from database.connection import db

def get_random_id(length: int = 10) -> str:
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

# MongoDB에 연결합니다.
collection = db.Beers

# print("---------------------xhruaazpkw"+"---------------------")
# asyncio.run(BeerRecommender.match_beers("xhruaazpkw"))
# print("---------------------htdmmmzobb"+"---------------------")
# asyncio.run(BeerRecommender.match_beers("htdmmmzobb"))
print("---------------------kvyzfrqhom"+"---------------------")
asyncio.run(BeerRecommender.match_beers("kvyzfrqhom"))

# #_---------------------------------------------------사용자선호도 샘플생성-----------------------------------------------------------------------------------------
# from random import choice, uniform
# unique_origins = ['덴마크', '멕시코', '영국', '체코', '벨기에', '네덜란드', '한국', '중국', '미국', '독일', '아일랜드', '일본']
# unique_categories = ['무알콜 맥주', '스타우트', '피스너', '밀맥주', '에일', '라거', '필스너', 'IPA']
# unique_food_pairings = ['타코', '버거', '그릴에 구운 소시지', '구운 고기', '스튜', '해산물', '피자', '독일식 프레첼', '바비큐', '치즈 플래터', '초밥', '한국식 바비큐', '나쵸', '스테이크', '샐러드', '피시앤칩스', '독일 소시지', '바베큐', '삼겹살', '돈까스', '빵과 치즈', '치즈', '라멘', '중국식 요리', '소시지', '후라이드 치킨', '양념치킨', '딤섬']
# unique_tastes = ['스파이시한', '홉의 향', '가벼운', '홉의 풍미', '탄산감', '깔끔한', '과일향', '크리미한', '진한', '풍부한', '맥아의 풍미', '균형 잡힌', '상쾌한', '깊은', '부드러운']

# users_collection = db['Users']
# preferences_collection = db['UserPreferences']

# async def create_preferences_documents():
#     user_ids = [user['user_id'] async for user in users_collection.find({}, {"_id": 0, "user_id": 1})]

#     for user_id in user_ids:
#         preferences = UserPreferences(
#             user_id=user_id,
#             preferred_origin=choice(unique_origins),
#             preferred_categories=[choice(unique_categories) for _ in range(3)],  # 3개의 선호 카테고리를 랜덤 선택
#             preferred_sweetness=round(uniform(1.0, 5.0), 1),  # 당도는 1.0에서 5.0 사이에서 랜덤 선택
#             preferred_bitterness=round(uniform(1.0, 5.0), 1),  # 쓴맛은 1.0에서 5.0 사이에서 랜덤 선택
#             preferred_sourness=round(uniform(1.0, 5.0), 1),  # 산미는 1.0에서 5.0 사이에서 랜덤 선택
#             preferred_ABV=round(uniform(0, 10), 2),  # 알코올 도수는 0에서 100 사이에서 랜덤 선택
#             preferred_food_pairing=[choice(unique_food_pairings) for _ in range(3)],  # 3개의 선호 음식 매칭을 랜덤 선택
#             preferred_taste=[choice(unique_tastes) for _ in range(3)]  # 3개의 선호 맛을 랜덤 선택
#         )

#         preferences_collection.insert_one(preferences.dict())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(create_preferences_documents())
# #_---------------------------------------------------사용자선호도 샘플생성-----------------------------------------------------------------------------------------

# async def get_unique_values(collection, field: str) -> List[str]:
#     pipeline = [
#         {"$group": {"_id": f"${field}"}},
#         {"$project": {"_id": 0, field: "$_id"}}
#     ]
#     return [doc[field] async for doc in collection.aggregate(pipeline)]

# async def print_unique_values():
#     unique_origins = await get_unique_values(collection, "origin")
#     unique_categories = await get_unique_values(collection, "category")
    
#     # List 타입 필드의 경우 $unwind를 사용해야 합니다.
#     pipeline = [{"$unwind": "$food_pairing"}, {"$group": {"_id": "$food_pairing"}}]
#     unique_food_pairings = [doc["_id"] async for doc in collection.aggregate(pipeline)]

#     pipeline = [{"$unwind": "$taste"}, {"$group": {"_id": "$taste"}}]
#     unique_tastes = [doc["_id"] async for doc in collection.aggregate(pipeline)]

#     print("Unique origins:", unique_origins)
#     print("Unique categories:", unique_categories)
#     print("Unique food pairings:", unique_food_pairings)
#     print("Unique tastes:", unique_tastes)

# # Run the async function
# import asyncio
# loop = asyncio.get_event_loop()
# loop.run_until_complete(print_unique_values())


# async def rearrange_fields(collection):
#     async for beer in collection.find():
#         new_beer = {
#             'beer_id': beer['beer_id'],
#             'name': beer['name'],
#             'origin': beer['origin'],
#             'category': beer['category'],
#             'sweetness': beer['sweetness'],
#             'bitterness': beer['bitterness'],
#             'sourness': beer['sourness'],
#             'ABV': beer['ABV'],
#             'food_pairing': beer['food_pairing'],
#             'taste': beer['taste'],
#             'image_path': beer['image_path'],
#             'rating': beer['rating']
#         }
#         await collection.replace_one({'_id': beer['_id']}, new_beer)

# # asyncio.run(rearrange_fields(collection))
