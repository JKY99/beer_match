from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
# from database.models import *
from database.database import *

app = FastAPI()

@app.get("/hello")
def hello():
    return {"Hello": "World"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#--------------------------------------Beer------------------------------------------
# 모든 맥주 목록을 반환하는 API 엔드포인트
@app.get("/beers", response_model=List[Beer])
async def get_all_beers():
    return await BeerService.read_all()

# 특정 ID의 맥주 정보를 반환하는 API 엔드포인트
@app.get("/beers/id/{beer_id}", response_model=Beer)
async def get_beer(beer_id: str):
    beer = await BeerService.read(beer_id)
    if beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return beer

# 맥주 이름으로 맥주를 찾는 API
@app.get("/beers/name/{beer_name}", response_model=Beer)
async def read_beer_by_name(beer_name: str):
    beer = await BeerService.read_by_name(beer_name)
    if beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return beer

# 새로운 맥주를 추가하는 API 엔드포인트
@app.post("/beers", response_model=Beer)
async def create_beer(beer: Beer):
    return await BeerService.create(beer)

# 특정 ID의 맥주 정보를 수정하는 API 엔드포인트
@app.put("/beers/{beer_id}", response_model=Beer)
async def update_beer(beer_id: str, beer: Beer):
    updated_beer = await BeerService.update(beer_id, beer)
    if updated_beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    return updated_beer

# 특정 ID의 맥주 정보를 삭제하는 API 엔드포인트
@app.delete("/beers/{beer_id}")
async def delete_beer(beer_id: str):
    beer = await BeerService.read(beer_id)
    if beer is None:
        raise HTTPException(status_code=404, detail="Beer not found")
    await BeerService.delete(beer_id)
    return {"message": "Beer has been deleted successfully"}

#--------------------------------------Beer------------------------------------------
#--------------------------------------User------------------------------------------

# 새 사용자를 생성하는 API
@app.post("/users", response_model=User)
async def create_user(user: User):
    return await UserService.create(user)

# 특정 ID를 가진 사용자를 가져오는 API
@app.get("/users/{user_id}", response_model=User)
async def read_user(user_id: str):
    user = await UserService.read(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 모든 사용자를 가져오는 API
@app.get("/users", response_model=List[User])
async def read_users():
    return await UserService.read_all()

# 특정 ID를 가진 사용자의 정보를 업데이트하는 API
@app.put("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user: User):
    updated_user = await UserService.update(user_id, user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

# 특정 ID를 가진 사용자를 삭제하는 API
@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    user = await UserService.read(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await UserService.delete(user_id)
    return {"message": "User has been deleted successfully"}

#--------------------------------------User------------------------------------------
#--------------------------------------UserSearchHistory------------------------------------------

@app.post("/search-history/", response_model=UserSearchHistory)
async def create_search_history(history: UserSearchHistory) -> UserSearchHistory:
    return await UserSearchHistoryService.create(history)

@app.get("/search-history/{user_id}", response_model=List[UserSearchHistory])
async def read_search_history_by_user_id(user_id: str) -> List[UserSearchHistory]:
    histories = await UserSearchHistoryService.read(user_id)
    if histories:
        return histories
    else:
        raise HTTPException(status_code=404, detail="Search histories not found")

@app.get("/search-historys/", response_model=List[UserSearchHistory])
async def read_all_search_histories() -> List[UserSearchHistory]:
    return await UserSearchHistoryService.read_all()

@app.delete("/search-history/{user_id}")
async def delete_search_history(user_id: str) -> None:
    await UserSearchHistoryService.delete(user_id)
    return {"message": "Search histories deleted"}

#--------------------------------------UserSearchHistory------------------------------------------
#--------------------------------------BeerRecommender------------------------------------------

@app.post("/recommend_beers/", response_model=List[Beer])
async def recommend_beers(user_id: str):
    beers = await BeerRecommender.match_beers(user_id)
    return beers

#--------------------------------------BeerRecommender------------------------------------------
#--------------------------------------UserFavoriteItem------------------------------------------

# UserFavorites 생성 API
@app.post("/user_favorites/", response_model=UserFavorites)
async def create_user_favorites(user_favorites: UserFavorites):
    return await UserFavoritesService.create(user_favorites)

# UserFavorites 조회 API
@app.get("/user_favorites/{user_id}", response_model=UserFavorites)
async def read_user_favorites(user_id: str):
    return await UserFavoritesService.read(user_id)

# 모든 UserFavorites 조회 API
@app.get("/user_favorites/", response_model=List[UserFavorites])
async def read_all_user_favorites():
    return await UserFavoritesService.read_all()

# UserFavorites 업데이트 API
@app.put("/user_favorites/{user_id}", response_model=UserFavorites)
async def update_user_favorites(user_id: str, user_favorites: UserFavorites):
    return await UserFavoritesService.update(user_id, user_favorites)

# UserFavorites 삭제 API
@app.delete("/user_favorites/{user_id}")
async def delete_user_favorites(user_id: str):
    await UserFavoritesService.delete(user_id)
    return {"message": "User favorites deleted successfully."}

#--------------------------------------UserFavoriteItem------------------------------------------


# # 찜한 정보를 조회합니다.   ex) /userfavorites?user_id=user1
# @app.get("/userfavorites/", response_model=UserFavorites)
# async def get_user_favorites(user_id: str = Query(...)):
#     result = await find_user_favorites(user_id)
#     return result

# # 찜한 맥주를 추가합니다.   ex) /userfavorites?user_id=user1&beer_id=beer123
# @app.post("/userfavorites/", response_model=UserFavorites)
# async def add_favorite_beer(user_id: str = Query(...), beer_id: str = Query(...)):
#     result = await add_favorite_beer(user_id, beer_id)
#     return result

# 이미지 파일 반환하기 ex) /data/img/카스.jpg
@app.get("/data/img/{filename}")
async def get_image(filename: str):
    return FileResponse(path=f"data/img/{filename}", media_type="image/jpeg")
