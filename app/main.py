from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

@app.get("/")
def home():
    return{"message": "Hello from FastAPI container!"}

@app.get("/db")
def db_check():
    try:
        clinet = MongoClient("mongodb://mongo:27017")
        db_names = clinet.list_database_names()
        return {"databases": db_names}
    except Exception as e:
        return {"error": str(e)}