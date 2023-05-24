from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 맥주 클래스 정의
class Beer:
    def __init__(self, name, sweetness, bitterness, sourness, ABV):
        self.name = name  # 맥주 이름
        self.sweetness = sweetness  # 당도
        self.bitterness = bitterness  # 쓴맛
        self.sourness = sourness  # 산미
        self.ABV = ABV  # 알코올 도수

# 사용자 선호도 클래스 정의
class UserPreferences:
    def __init__(self, preferred_sweetness, preferred_bitterness, preferred_sourness, preferred_ABV):
        self.preferred_sweetness = preferred_sweetness  # 선호 당도
        self.preferred_bitterness = preferred_bitterness  # 선호 쓴맛
        self.preferred_sourness = preferred_sourness  # 선호 산미
        self.preferred_ABV = preferred_ABV  # 선호 알코올 도수

# 맥주 목록 생성
beers = [
    Beer("Beer1", 7.0, 5.0, 3.0, 4.5),
    Beer("Beer2", 5.0, 6.0, 4.0, 5.0),
    Beer("Beer3", 6.0, 7.0, 4.0, 4.0),
    Beer("Beer4", 8.0, 6.0, 3.5, 5.5),
    Beer("Beer5", 4.0, 7.0, 5.0, 6.0),
    Beer("Beer6", 5.5, 5.0, 4.0, 4.7),
    Beer("Beer7", 6.5, 4.0, 3.0, 5.2),
    Beer("Beer8", 7.0, 6.0, 3.0, 4.8),
    Beer("Beer9", 5.0, 5.5, 4.5, 4.9),
    Beer("Beer10", 6.0, 6.5, 3.5, 5.0),
    Beer("Beer11", 6.5, 6.0, 3.5, 4.6),
    Beer("Beer12", 5.5, 5.5, 4.0, 5.3),
    Beer("Beer13", 6.0, 6.0, 4.0, 5.5),
    Beer("Beer14", 7.0, 5.0, 3.5, 4.7),
    Beer("Beer15", 6.5, 5.5, 3.5, 5.0)
]

# 사용자 선호도 생성
user_pref = UserPreferences(2.0, 6.0, 3.5, 4.5)

# 맥주 및 사용자 선호도를 벡터화
beer_vectors = np.array([[b.sweetness, b.bitterness, b.sourness, b.ABV] for b in beers])
user_vector = np.array([user_pref.preferred_sweetness, user_pref.preferred_bitterness, user_pref.preferred_sourness, user_pref.preferred_ABV])

# 코사인 유사도 계산
similarities = cosine_similarity(beer_vectors, user_vector.reshape(1, -1)).flatten()

# 유사도 순서대로 맥주들의 인덱스를 가져옵니다.
sorted_beer_indexes = np.argsort(similarities)[::-1]

# 유사도 순으로 맥주를 출력합니다.
for idx in sorted_beer_indexes:
    print(f"Beer: {beers[idx].name}, Similarity: {similarities[idx]}")
