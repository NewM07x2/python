# curl -X POST -H "Content-Type: application/json" -d '{"title":"Sample Todo"}' http://localhost:8000/    
# curl -X GET http://localhost:8000/    


from fastapi import FastAPI, Depends

from app.schemas.dbConnect import SessionLocal

from app.service.customerService import CustomerService

app = FastAPI()
# クラスを定義
customerService = CustomerService()

def DBConnect():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}C


@app.get("/test")
def read_test():
    msg = "Hello FastAPI test"
    print(msg)  # ターミナルに表示
    return {"message": "Hello FastAPI test"}

@app.get("/get/customer")
def get_customer():
    data = customerService.getCustomerData()
    print(data)  # ターミナルに表示
    return data

@app.get("/test-db")
def test_db(db=Depends(DBConnect)):
    # ここでdbを使ってDB操作が可能

    return {"status": "connected"}