# import asyncio
from fastapi import FastAPI, Query, Path
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime
from models import Beer, UserFavorites
from database import find_all_beers, find_beer, find_user_favorites

app = FastAPI()
# app.mount("/", StaticFiles(directory="public", html = True), name="static")\

@app.get("/hello")
def hello():
    return {"Hello": "World"}

# 모든 맥주 정보를 조회합니다.  ex) /beers/all
@app.get("/beers/all", response_model=List[Beer])
async def get_all_beers():
    result = await find_all_beers()
    return result

# 맥주 정보를 조회합니다.   ex) /beers?beer_name=cass
@app.get("/beers/", response_model=Beer)
async def get_beer_by_name(beer_name: str = Query(...)):
    result = await find_beer(beer_name)
    return result

# 찜한 정보를 조회합니다.   ex) /userfavorites?user_id=user1
@app.get("/userfavorites/", response_model=UserFavorites)
async def get_user_favorites(user_id: str = Query(...)):
    result = await find_user_favorites(user_id)
    return result

# 찜한 맥주를 추가합니다.   ex) /userfavorites?user_id=user1&beer_id=beer123
@app.post("/userfavorites/", response_model=UserFavorites)
async def add_favorite_beer(user_id: str = Query(...), beer_id: str = Query(...)):
    result = await add_favorite_beer(user_id, beer_id)
    return result

# 이미지 파일 반환하기 ex) /data/img/카스.jpg
@app.get("/data/img/{filename}")
async def get_image(filename: str = Path(...)):
    return FileResponse(path=f"data/img/{filename}", media_type="image/jpeg")