from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {'message':'Hello World'}

@app.get("/about")
def about():
    return{'message':'Hello i m akshit i curruntly Learning AI'}

@app.get("/reload")
def reload():
    return{'message':'hello'}

@app.get("/items/{item_id}")
def read_item(item_id: int, item_name: str | None = None):
    return {"item_id": item_id, "item_name": item_name}