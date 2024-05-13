from fastapi import FastAPI,Request
from pydantic import BaseModel
from utils import *
from login import *
import JWT_helper
import SQL_helper
app = FastAPI()

class Item(BaseModel):
    url: str

class login_Item(BaseModel):
    code: str
    data: str
    iv: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/api/video-parse")
async def video_parse(json:Item):
    print(json.url)
    video_url = video_parse_url(json.url)
    # video_url = "a"
    # print(type(video_url))
    return video_url

@app.post("/api/auth/login")
async def auth_login(json:login_Item):
    UserInfo = login(json.code,json.data,json.iv)
    print(UserInfo)
    openId = UserInfo["openId"]

    data = {
        'token': JWT_helper.creat_token(openId),
    }
    print(data)
    return data


@app.get("/api/records/total")
async def records_total(request: Request):
    print(request.headers.get("Authorization"))
    print('aaa')
    total_num = SQL_helper.fetchall('select total_num from USER_INFO')
    json = {
        "total_num": total_num,
    }
    return json
