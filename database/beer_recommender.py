from typing import List
from numpy import dot
from numpy.linalg import norm
from database.connection import *
from database.models import *

class BeerRecommender:
    # 원-핫 인코딩 함수
    @classmethod
    def one_hot_encode(cls, value: str, categories: List[str]) -> List[int]:
        return [1 if category == value else 0 for category in categories]

    # 코사인 유사도 계산 함수
    @classmethod
    def cosine_similarity(cls, a: List[int], b: List[int]) -> float:
        return dot(a, b) / (norm(a) * norm(b))

    @classmethod
    async def match_beers(cls, user_id: str) -> List[Beer]:
        #사용자 선호도에 맞춘 맥주 추천 함수
        cls.db = db
        cls.beers = db.Beers
        cls.user_preferences = db.UserPreferences
        cls.unique_origins = ['덴마크', '멕시코', '영국', '체코', '벨기에', '네덜란드', '한국', '중국', '미국', '독일', '아일랜드', '일본']
        cls.unique_categories = ['무알콜 맥주', '스타우트', '피스너', '밀맥주', '에일', '라거', '필스너', 'IPA']
        cls.unique_food_pairings = ['타코', '버거', '그릴에 구운 소시지', '구운 고기', '스튜', '해산물', '피자', '독일식 프레첼', '바비큐', '치즈 플래터', '초밥', '한국식 바비큐',
                                     '나쵸', '스테이크', '샐러드', '피시앤칩스', '독일 소시지', '바베큐', '삼겹살', '돈까스', '빵과 치즈', '치즈', '라멘', '중국식 요리', '소시지', '후라이드 치킨', '양념치킨', '딤섬']
        cls.unique_tastes = ['스파이시한', '홉의 향', '가벼운', '홉의 풍미', '탄산감', '깔끔한', '과일향', '크리미한', '진한', '풍부한', '맥아의 풍미', '균형 잡힌', '상쾌한', '깊은', '부드러운']

        # 모든 맥주 정보와 해당 사용자의 선호도를 가져옵니다.
        beer_list = await cls.beers.find().to_list(length=1000)
        user_preference = await cls.user_preferences.find_one({'user_id': user_id})

        # 사용자 선호도가 없을 경우 None을 반환합니다.
        if not user_preference:
            return None

        # 사용자 선호도를 벡터화합니다.
        user_vector = [
            user_preference['preferred_sweetness'],
            user_preference['preferred_bitterness'],
            user_preference['preferred_sourness'],
            user_preference['preferred_ABV']
        ]
        user_vector += cls.one_hot_encode(user_preference['preferred_origin'], cls.unique_origins)
        user_vector += cls.one_hot_encode(user_preference['preferred_categories'], cls.unique_categories)
        user_vector += cls.one_hot_encode(user_preference['preferred_food_pairing'], cls.unique_food_pairings)
        user_vector += cls.one_hot_encode(user_preference['preferred_taste'], cls.unique_tastes)

        result_list = []

        # 모든 맥주를 돌면서 각 맥주와 사용자 선호도의 유사도를 계산합니다.
        for beer in beer_list:
            beer_vector = [
                beer['sweetness'],
                beer['bitterness'],
                beer['sourness'],
                beer['ABV']
            ]
            beer_vector += cls.one_hot_encode(beer['origin'], cls.unique_origins)
            beer_vector += cls.one_hot_encode(beer['category'], cls.unique_categories)
            beer_vector += cls.one_hot_encode(beer['food_pairing'], cls.unique_food_pairings)
            beer_vector += cls.one_hot_encode(beer['taste'], cls.unique_tastes)

            similarity = cls.cosine_similarity(user_vector, beer_vector)
            print(beer["name"]+": "+str(similarity))
            result_list.append((beer, similarity))  # 맥주와 그 유사도를 리스트에 추가

        # 유사도가 높은 순으로 정렬합니다.
        result_list.sort(key=lambda x: x[1], reverse=True)

        return [beer for beer, _ in result_list]  # 맥주만 반환
