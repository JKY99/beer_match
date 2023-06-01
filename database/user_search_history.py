from typing import List
from database.models import UserSearchHistory
from database.connection import db

# UserSearchHistoryService는 UserSearchHistory 컬렉션에 대한 CRUD 연산을 수행합니다.
class UserSearchHistoryService:
    # 'UserSearchHistorys'라는 이름의 MongoDB 컬렉션을 참조합니다.
    collection = db['UserSearchHistorys']

    # create 메소드는 UserSearchHistory 객체를 받아서 MongoDB에 저장합니다.
    @classmethod
    async def create(cls, history: UserSearchHistory) -> UserSearchHistory:
        # UserSearchHistory 객체를 dictionary 형태로 변환합니다.
        history_dict = history.dict()
        # 변환된 dictionary를 MongoDB에 삽입합니다.
        await cls.collection.insert_one(history_dict)
        # 삽입된 UserSearchHistory 객체를 반환합니다.
        return history

    # read 메소드는 사용자 ID를 받아서 해당 사용자의 모든 검색 기록을 MongoDB에서 찾아 반환합니다.
    @classmethod
    async def read(cls, user_id: str) -> List[UserSearchHistory]:
        # MongoDB에서 user_id와 일치하는 모든 검색 기록을 찾습니다.
        histories = await cls.collection.find({"user_id": user_id}).to_list(length=1000)
        # 찾은 검색 기록을 UserSearchHistory 객체로 변환하여 리스트 형태로 반환합니다.
        return [UserSearchHistory(**history) for history in histories]

    # read_all 메소드는 MongoDB에 있는 모든 검색 기록을 반환합니다.
    @classmethod
    async def read_all(cls) -> List[UserSearchHistory]:
        # MongoDB에서 모든 검색 기록을 찾습니다.
        histories = await cls.collection.find().to_list(length=10000)
        # 찾은 검색 기록을 UserSearchHistory 객체로 변환하여 리스트 형태로 반환합니다.
        return [UserSearchHistory(**history) for history in histories]

    # delete 메소드는 사용자 ID를 받아서 해당 사용자의 모든 검색 기록을 MongoDB에서 삭제합니다.
    @classmethod
    async def delete(cls, user_id: str) -> None:
        # MongoDB에서 user_id와 일치하는 모든 검색 기록을 삭제합니다.
        await cls.collection.delete_many({"user_id": user_id})
