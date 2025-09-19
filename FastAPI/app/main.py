# curl -X POST -H "Content-Type: application/json" -d '{"title":"Sample Todo"}' http://localhost:8000/    
# curl -X GET http://localhost:8000/    


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


@app.get("/test")
def read_test():
    msg = "Hello FastAPI test"
    print(msg)  # ターミナルに表示
    return {"message": "Hello FastAPI test"}
