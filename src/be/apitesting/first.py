from typing import Union

from fastapi import FastAPI,Request,Query

app = FastAPI()


@app.get("/warn_users")
def read_root():
    return {"Deployed initial piece of Api code!"}


@app.get("/topics/")
async def read_items(q: str | None = Query(default=..., min_length=3)):
    results = {"topics": [{"topic_id": "Foo"}, {"topic_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.post("/users")
async def users(info : Request):
    req_info = await info.json()
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }

#it is an api for contact details form..User can fill details here.

@app.post("/contactus")
async def contactus(info : Request):
    req_info = await info.json()

    return{
        "status":"SUCCESS",
        "data":req_info
    }

@app.post("/search")
async def search(info:Request):
    search_string = await info.json()

    return {
        "status":"SUCCESS",
        "data":search_string +"found"
    }


