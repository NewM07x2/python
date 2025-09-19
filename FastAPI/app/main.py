from fastapi import FastAPI
from api import api_router


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/test")
def read_test():
    return {"message": "Hello FastAPI test"}
