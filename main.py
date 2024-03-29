import requests
import uuid
import time
import json
import uvicorn
import urllib.request
import urllib.parse


from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

NAVER_CLIENT_ID = "ApiPimNUJywHK4ZJe0hE"
NAVER_CALLBACK_URL = "http://localhost:8080/login/naver"
NAVER_INGA_URL = "https://nid.naver.com/oauth2.0/authorize?"

origins = [
    # "http://localhost:8080",  # mohaet local
    # "http://localhost:3000",
    # "http://localhost:5050",
    # "http://localhost",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Images(BaseModel):
    code: str
    state: str


@app.get('/url')
def getUrl():
    data = {
        'response_type': "code",
        'client_id': NAVER_CLIENT_ID,
        'redirect_uri': NAVER_CALLBACK_URL,
        'state': 'test'
    }
    total_data = urllib.parse.urlencode(data)
    url = NAVER_INGA_URL + total_data
    # req = urllib.request.Request(url)
    # response = urllib.request.urlopen(req)
   
    return url
@app.get('url/getToken')
def GetToken():

    return 
# @app.get('/url/getToken')
# def getToken(data: Images):
#     print(data)
    
#     return data
    


async def intoTheNaver(data: Images):
    print("here-----> ", data)

    # res = requests.request("GET", data)
    # print(res)
    # return res


if __name__ == "__main__":
    uvicorn.run("router_example:app", host='0.0.0.0', port=8000, reload=True)