from typing import List
from database.models import User
from database.connection import db
from bson.objectid import ObjectId

# 사용자에 대한 CRUD 연산을 수행하는 UserService 클래스입니다.
class UserService:
    # MongoDB의 users 컬렉션을 참조합니다.
    collection = db['users']

    # 새로운 사용자를 생성하고 반환하는 메서드입니다.
    @classmethod
    async def create(cls, user: User) -> User:
        user_dict = user.dict()  # User pydantic 모델을 딕셔너리로 변환합니다.
        user_dict["_id"] = ObjectId()  # 새로운 MongoDB ObjectId를 생성합니다.
        await cls.collection.insert_one(user_dict)  # users 컬렉션에 새 문서를 삽입합니다.
        return user  # 생성된 User 모델을 반환합니다.

    # 주어진 ID에 해당하는 사용자를 찾고 반환하는 메서드입니다.
    @classmethod
    async def read(cls, user_id: str) -> User:
        # users 컬렉션에서 _id 필드가 user_id와 일치하는 문서를 찾습니다.
        user = await cls.collection.find_one({"_id": ObjectId(user_id)})
        # 찾은 문서가 있으면 User 모델로 변환하고 반환하고, 없으면 None을 반환합니다.
        return User(**user) if user else None

    # 모든 사용자를 찾아 반환하는 메서드입니다.
    @classmethod
    async def read_all(cls) -> List[User]:
        # users 컬렉션의 모든 문서를 찾아 최대 100개까지 리스트로 변환합니다.
        users = await cls.collection.find().to_list(length=100)
        # 각 문서를 User 모델로 변환하여 리스트로 만들고 반환합니다.
        return [User(**user) for user in users]

    # 주어진 ID에 해당하는 사용자의 정보를 업데이트하고 업데이트된 사용자를 반환하는 메서드입니다.
    @classmethod
    async def update(cls, user_id: str, user: User) -> User:
        # users 컬렉션에서 _id 필드가 user_id와 일치하는 문서를 user의 정보로 교체합니다.
        await cls.collection.replace_one({"_id": ObjectId(user_id)}, user.dict())
        # 업데이트된 사용자를 찾아서 반환합니다.
        return await cls.read(user_id)

    # 주어진 ID에 해당하는 사용자를 삭제하는 메서드입니다.
    @classmethod
    async def delete(cls, user_id: str) -> None:
        # users 컬렉션에서 _id 필드가 user_id와 일치하는 문서를 삭제합니다.
        await cls.collection.delete_one({"_id": ObjectId(user_id)})
