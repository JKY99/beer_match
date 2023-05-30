from typing import List
from database.models import User
from database.connection import db
from bson.objectid import ObjectId

# 사용자에 대한 CRUD 연산을 수행하는 UserService 클래스입니다.
class UserService:
    collection = db['Users']

    @classmethod
    async def create(cls, user: User) -> User:
        user_dict = user.dict()
        await cls.collection.insert_one(user_dict)
        return user

    @classmethod
    async def read(cls, user_id: str) -> User:
        user = await cls.collection.find_one({"user_id": user_id})
        return User(**user) if user else None

    @classmethod
    async def read_all(cls) -> List[User]:
        users = await cls.collection.find().to_list(length=100)
        return [User(**user) for user in users]

    @classmethod
    async def update(cls, user_id: str, user: User) -> User:
        await cls.collection.replace_one({"user_id": user_id}, user.dict())
        return await cls.read(user.user_id)

    @classmethod
    async def delete(cls, user_id: str) -> None:
        await cls.collection.delete_one({"user_id": user_id})