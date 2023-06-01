from datetime import datetime

from database.beer import *
from database.user import *
from database.user_search_history import *
from database.beer_recommender import *
from database.user_favorite_item import *
from database.beer_service import *

from database.connection import *
from database.models import *

async def find_user_favorites(user_id: str) -> dict:
    user_favorites = db.UserFavorites
    result = await user_favorites.find_one({'user_id': user_id})
    return result

async def add_favorite_beer(user_id: str, beer_name: str) -> dict:
    user_favorites = db.UserFavorites
    result = await user_favorites.find_one({'user_id': user_id})
    current_time = datetime.utcnow()  # 찜한 시간을 UTC 기준으로 저장합니다.
    new_favorite = {'name': beer_name, 'timestamp': current_time}  # 새로운 찜 항목을 생성합니다.

    # 해당 user_id가 이미 존재하는 경우
    if result:
        # 이미 찜 목록에 favoriteBeerIDs 항목이 있고, 아직 해당 맥주가 추가되지 않은 경우
        if 'favoriteBeerIDs' in result and not any(beer['name'] == beer_name for beer in result['favoriteBeerIDs']):
            # 해당 맥주를 찜 목록에 추가합니다.
            result['favoriteBeerIDs'].append(new_favorite)
            
            # MongoDB에서 해당 문서를 업데이트합니다.
            await user_favorites.update_one({'user_id': user_id}, {'$set': result})
        # 찜 목록에 favoriteBeerIDs 항목이 없는 경우
        elif 'favoriteBeerIDs' not in result:
            # 새로운 favoriteBeerIDs 항목을 생성하고, 해당 맥주를 추가합니다.
            result['favoriteBeerIDs'] = [new_favorite]
            
            # MongoDB에서 해당 문서를 업데이트합니다.
            await user_favorites.update_one({'user_id': user_id}, {'$set': result})
    # 해당 user_id가 존재하지 않는 경우
    else:
        # 새로운 문서를 생성하여 MongoDB에 추가합니다.
        await user_favorites.insert_one({'user_id': user_id, 'favoriteBeerIDs': [new_favorite], 'favoriteNewsIDs': []})
    
    # 업데이트된 문서를 반환합니다.
    return await user_favorites.find_one({'user_id': user_id})
