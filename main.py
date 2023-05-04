from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"msg": "hello, world!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"status": "success", "message": "hello, %s!" % (name)}
