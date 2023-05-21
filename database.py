from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv, find_dotenv
import os
import asyncio

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

uri = f"mongodb+srv://admin:{password}@recommend.wg2l4em.mongodb.net/?retryWrites=true&w=majority"

client = AsyncIOMotorClient(uri)


# 데이터베이스를 선택합니다.
db = client.BeerRecommendationsDB

async def fetch_beers():
    beers = await db["beers"].find().to_list(1000)
    return beers

async def insert_beer(beer):
    await db["beers"].insert_one(beer.dict())



#######################################
# import json,sys,io
# sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')
#######################################
# # Beers 컬렉션 선택
# collection = db.Beers

# # JSON 파일을 읽습니다.
# with open('C:\\Users\\jkypc\\OneDrive\\문서\\1.대학(3-1)\\전공_캡스톤디자인1\\fastapi_0519\data\\beers.json',encoding="UTF-8") as f:
#     data = json.load(f)

#     # JSON 데이터를 읽어와서 각 맥주를 MongoDB 컬렉션에 개별 문서로 넣습니다.
#     for beer in data:
#         collection.insert_one(beer)
#######################################
# # Users 컬렉션 선택
# collection = db.Users
# # JSON 파일을 읽습니다.
# with open('C:\\Users\\jkypc\\OneDrive\\문서\\1.대학(3-1)\\전공_캡스톤디자인1\\fastapi_0519\data\\users.json',encoding="UTF-8") as f:
#     data = json.load(f)

#     # JSON 데이터를 읽어와서 각 맥주를 MongoDB 컬렉션에 개별 문서로 넣습니다.
#     for user in data:
#         collection.insert_one(user)
#######################################

# async def find_all_beers():
#     beers = db.beers
#     beer_list = await list(beers.find())
#     return beer_list

async def find_all_beers():
    beers = db.Beers
    beer_list = await beers.find().to_list(length=1000)
    return beer_list

async def find_beer(beer_name):
    beers = db.Beers
    beer = await beers.find_one({'name': beer_name})
    return beer

async def find_user_favorites(user_id: str) -> dict:
    user_favorites = db.UserFavorites
    result = await user_favorites.find_one({'user_id': user_id})
    return result

async def add_favorite_beer(user_id: str, beer_id: str) -> dict:
    user_favorites = db.UserFavorites
    result = await user_favorites.find_one({'user_id': user_id})

    # 해당 user_id가 이미 존재하는 경우
    if result:
        # 이미 찜 목록에 favoriteBeerIDs 항목이 있고, 아직 해당 맥주가 추가되지 않은 경우
        if 'favoriteBeerIDs' in result and beer_id not in result['favoriteBeerIDs']:
            # 해당 맥주를 찜 목록에 추가합니다.
            result['favoriteBeerIDs'].append(beer_id)
            
            # MongoDB에서 해당 문서를 업데이트합니다.
            await user_favorites.update_one({'user_id': user_id}, {'$set': result})
        # 찜 목록에 favoriteBeerIDs 항목이 없는 경우
        elif 'favoriteBeerIDs' not in result:
            # 새로운 favoriteBeerIDs 항목을 생성하고, 해당 맥주를 추가합니다.
            result['favoriteBeerIDs'] = [beer_id]
            
            # MongoDB에서 해당 문서를 업데이트합니다.
            await user_favorites.update_one({'user_id': user_id}, {'$set': result})
    # 해당 user_id가 존재하지 않는 경우
    else:
        # 새로운 문서를 생성하여 MongoDB에 추가합니다.
        await user_favorites.insert_one({'user_id': user_id, 'favoriteBeerIDs': [beer_id], 'favoriteNewsIDs': []})
    
    # 업데이트된 문서를 반환합니다.
    return await user_favorites.find_one({'user_id': user_id})