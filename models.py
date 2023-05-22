from datetime import datetime
from typing import List, Optional, Dict
from pydantic import BaseModel, Field, EmailStr

class Beer(BaseModel):
    name: str
    origin: str             # 원산지 (국산 또는 수입)
    category: str           # 맥주 대분류 (예: 에일, 라거)
    sweetness: float        # 당도
    bitterness: float       # 쓴맛 
    sourness: float         # 산미
    ABV: float = Field(..., ge=0, le=100)  # 맥주 알코올 도수, 0~100% 범위
    food_pairing: List[str] # 맥주와 잘 어울리는 음식
    taste: List[str]        # 맥주의 특징적인 맛과 향에 대한 설명
    image_path: str         # 맥주 이미지 경로
    rating: float           # 평점

# 사용자 정보를 담는 BaseModel입니다.
class User(BaseModel):
    user_id: str                 # 사용자 ID
    email: EmailStr              # 사용자 이메일 주소, 유효한 이메일 형식 필요
    password: str           # 사용자 비밀번호 해시
    age: int = Field(..., gt=0)  # 사용자 나이, 양의 정수 필요
    gender: str                  # 사용자 성별

# 사용자의 맥주 검색 기록을 담는 BaseModel입니다.
class UserSearchHistory(BaseModel):
    user_id: str          # 사용자 ID (Users 테이블과 관련됨)
    search_query: str     # 사용자가 검색한 쿼리 문자열
    search_time: datetime = Field(default_factory=datetime.utcnow)  # 검색 시간, UTC 기준

# 사용자의 선호도 정보를 담는 BaseModel입니다.
class UserPreferences(BaseModel):
    user_id: str                     # 사용자 ID
    preferred_origin: str            # 선호하는 원산지
    preferred_categories: List[str]  # 선호하는 맥주 대분류
    preferred_sweetness: float       # 선호하는 당도
    preferred_bitterness: float      # 선호하는 쓴맛
    preferred_sourness: float        # 선호하는 산미
    preferred_ABV: float             # 선호하는 알코올 도수
    preferred_food_pairing: List[str] # 선호하는 음식 매칭
    preferred_taste: List[str]       # 선호하는 맛과 향

# 사용자의 찜을 담는 BaseModel입니다.
class FavoriteItem(BaseModel):
    name: str
    timestamp: datetime

# 사용자의 찜한 정보들을 담는 BaseModel입니다.
class UserFavorites(BaseModel):
    user_id: str
    favoriteBeerIDs: Optional[List[FavoriteItem]] = Field(default=[])  # 사용자가 찜한 맥주의 ID와 찜한 시간
    favoriteNewsIDs: Optional[List[FavoriteItem]] = Field(default=[])  # 사용자가 찜한 뉴스의 ID와 찜한 시간