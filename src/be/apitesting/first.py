from typing import Union

from fastapi import FastAPI,Request,Query

app = FastAPI()

const articles = ["article 1 displays about security measures","article 2 displays about innovative approaches on authenticative measures"]
const title_array = [{"title":"Details page1","description":"We describe the details of page1 and its pros and cons","bg-img-url":"dummy.png"},{},{}]

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

@app.post("/articles")
async def articles(info:Request):
    temp = await info.json()

    return{
        "status":"SUCCESS",
        "data":articles
    }

@app.post("/details_page")
async def details(info:Request):
    result = await info.json()

    return{
        "status":"SUCCESS",
        "data":title_array
    }
###Response:---
# {"status":"SUCCESS","data":[{"title":"Details page1","description":"We describe the details of page1 and its pros and cons","img-url":"dummy.png"},{},{}]}