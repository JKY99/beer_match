import random
import string
import json
from typing import Dict, List
from models import User

# 이메일 생성을 위한 도메인 리스트
domains = ["gmail.com", "naver.com", "daum.net", "yahoo.com", "korea.com"]

# 랜덤한 문자열을 생성하는 함수
def random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

users = []
for i in range(20):
    user_id = random_string(10)
    email = f"{random_string(5)}@{random.choice(domains)}"
    password = random_string(10)
    age = random.randint(20, 50)
    gender = random.choice(["남성", "여성"])
    users.append(
        User(
            user_id=user_id,
            email=email,
            password=password,
            age=age,
            gender=gender
        )
    )

# Pydantic User 객체 리스트를 Python 딕셔너리 리스트로 변환
users_dicts: List[Dict] = [user.dict() for user in users]

# JSON 파일로 저장
with open('data/users.json', 'w', encoding='utf-8') as f:
    json.dump(users_dicts, f, ensure_ascii=False, indent=4)
