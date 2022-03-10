from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

@app.get('/')
def index():
    return {"data":{"name":"ankit"}}

@app.get('/about')
def about():
    return {"data":"about page"}

@app.get('/blog')
def query(limit, published:bool):
    print(published)
    if published:
        print("yes")
        return {'data':f'{limit}published blog from the db'}
    else:
        print("no")
        return {'data':f'{limit} all the blog from the db'}

@app.get('/blog/{id}')
def show(id:int):
    return {"data":{id}}

class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool]

@app.post('/blog')
def create_blog(blog:Blog):
    return {'data': F'Blog is created as my{request.title}'}


if __name__="__main__":
    uvicorn.run(app,host="127.0.0.1",port='9000')