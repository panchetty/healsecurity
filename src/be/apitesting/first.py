from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/warn_users")
def read_root():
    return {"Deployed initial piece of Api code!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.put("/users/{user_id}")
def send_warning(user_id: int):
    return {"someone tried to malfunction your login details, reference user id": user_id}
    
@app.post("/items")
async def getInformation(info : Request):
    req_info = await info.json()
    return {
        "status" : "SUCCESS",
        "data" : req_info
    }
