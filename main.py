from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get('/')
def root():
    return "Hello World"   # 문자열 반환

@app.get('/json')
def printJson():
    return {"Number": 12345}  # (key, value) 객체 반환

@app.get("/home/{name}")
def read_name(name:str):
    return {'name': name}

@app.get("/home_err/{name}")
def read_name_err(name:int):
    return {'name': name}

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, "message": "Deep Learning FTW!"}
    if model_name.value == 'lenet':
        return {'model_name': model_name, "message": "LeCNN all the images"}
    return {"model_name": model_name, "message": "Have some residuals"}