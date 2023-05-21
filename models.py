from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, EmailStr

# 맥주 정보를 담는 BaseModel입니다.
# class Beer(BaseModel):
#     beer_name: str          # 맥주 이름
#     origin: str             # 맥주 원산지 (국산 또는 수입)
#     category: str           # 맥주 대분류 (예: 에일, 라거)
#     ABV: float = Field(..., ge=0, le=100)  # 맥주 알코올 도수, 0~100% 범위
#     taste: str              # 맥주 맛과 향에 대한 설명
#     food_pairing: str       # 맥주와 잘 어울리는 안주
#     image_path: str         # 맥주 이미지 파일 경로 또는 URL
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
    user_id: str            # 사용자 ID (Users 테이블과 관련됨)
    preferred_origin: Optional[List[str]] = []  # 선호하는 맥주의 원산지 리스트
    preferred_category: Optional[List[str]] = []  # 선호하는 맥주의 카테고리 리스트
    preferred_subcategory: Optional[List[str]] = []  # 선호하는 맥주의 부카테고리 리스트
    preferred_ABV: Optional[List[float]] = []  # 선호하는 맥주의 알코올 도수 범위 (예: [4.0, 6.0] - 4~6% 선호)
    preferred_tastes: Optional[List[str]] = []  # 선호하는 맥주의 맛 특성 리스트 (예: ["달콤한", "과일향"])
    preferred_food_pairings: Optional[List[str]] = []  # 선호하는 맥주와의 안주 조합 리스트

# 사용자의 찜한 정보를 담는 BaseModel입니다.
class UserFavorites(BaseModel):
    user_id: str
    favoriteBeerIDs: Optional[List[str]] = []  # 사용자가 찜한 맥주의 ID 리스트
    favoriteNewsIDs: Optional[List[str]] = []  # 사용자가 찜한 뉴스의 ID 리스트