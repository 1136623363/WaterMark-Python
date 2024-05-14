from datetime import datetime

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
    result = SQL_helper.fetchall('SELECT * FROM USER_INFO WHERE openId = %s',(openId,))
    if len(result) != 0 :
        join_date = datetime.now().date()
        total_num = 0
        last_use_time = datetime.now()
        result = SQL_helper.execute('INSERT INTO USER_INFO (openId, join_date, total_num, last_use_time) VALUES (%s, %s, %s, %s)',
                         openId, join_date, total_num, last_use_time)
    data = {
        'token': JWT_helper.creat_token(openId),
    }
    print(data)
    return data


@app.get("/api/records/total")
async def records_total(request: Request):
    authorization = request.headers.get("Authorization")
    # print(authorization)

    openId = JWT_helper.validate_token(authorization)

    total_num = SQL_helper.fetchall('SELECT total_num FROM USER_INFO WHERE openId = %s',(openId,))

    json = {
        "total_num": total_num,
    }

    return json
