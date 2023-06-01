from typing import List
from database.models import UserSearchHistory
from database.connection import db

class UserSearchHistoryService:
    # MongoDB에 있는 'UserSearchHistory'라는 이름의 컬렉션을 참조하도록 설정합니다.
    collection = db['UserSearchHistorys']

    @classmethod
    async def create(cls, history: UserSearchHistory) -> UserSearchHistory:
        history_dict = history.dict()
        await cls.collection.insert_one(history_dict)
        return history

    @classmethod
    async def read(cls, history_id: str) -> UserSearchHistory:
        history = await cls.collection.find_one({"history_id": history_id})
        return UserSearchHistory(**history) if history else None

    @classmethod
    async def read_all(cls) -> List[UserSearchHistory]:
        histories = await cls.collection.find().to_list(length=100)
        return [UserSearchHistory(**history) for history in histories]

    @classmethod
    async def update(cls, history_id: str, history: UserSearchHistory) -> UserSearchHistory:
        await cls.collection.replace_one({"history_id": history_id}, history.dict())
        return await cls.read(history_id)

    @classmethod
    async def delete(cls, history_id: str) -> None:
        await cls.collection.delete_one({"history_id": history_id})
