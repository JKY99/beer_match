# user_favorites.py
from typing import List
from database.models import UserFavorites
from database.connection import db

# UserFavorites에 대한 CRUD 연산을 수행하는 UserFavoritesService 클래스입니다.
class UserFavoritesService:
    collection = db['UserFavorites']

    @classmethod
    async def create(cls, user_favorites: UserFavorites) -> UserFavorites:
        # UserFavorites 모델 인스턴스를 딕셔너리로 변환하고 데이터베이스에 추가
        user_favorites_dict = user_favorites.dict()
        await cls.collection.insert_one(user_favorites_dict)
        return user_favorites

    @classmethod
    async def read(cls, user_id: str) -> UserFavorites:
        # user_id에 해당하는 UserFavorites를 데이터베이스에서 찾음
        user_favorites = await cls.collection.find_one({"user_id": user_id})
        return UserFavorites(**user_favorites) if user_favorites else None

    @classmethod
    async def read_all(cls) -> List[UserFavorites]:
        # 모든 UserFavorites를 데이터베이스에서 찾음
        user_favorites_list = await cls.collection.find().to_list(length=100)
        return [UserFavorites(**user_favorites) for user_favorites in user_favorites_list]

    @classmethod
    async def update(cls, user_id: str, user_favorites: UserFavorites) -> UserFavorites:
        # user_id에 해당하는 UserFavorites를 user_favorites 인스턴스로 업데이트
        await cls.collection.replace_one({"user_id": user_id}, user_favorites.dict())
        return await cls.read(user_favorites.user_id)

    @classmethod
    async def delete(cls, user_id: str) -> None:
        # user_id에 해당하는 UserFavorites를 데이터베이스에서 삭제
        await cls.collection.delete_one({"user_id": user_id})
