import os

from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pymongo.errors import PyMongoError

app = FastAPI(title="FastAPI and MongoDB Docker Demo")


@app.get("/")
def home():
    return {"message": "Hello from FastAPI container!"}


@app.get("/db")
def db_check():
    try:
        with MongoClient(os.environ["MONGO_URI"], serverSelectionTimeoutMS=5000) as client:
            client.admin.command("ping")
        return {"status": "connected", "database": "MongoDB"}
    except (PyMongoError, KeyError) as exc:
        raise HTTPException(status_code=503, detail="MongoDB connection unavailable") from exc
