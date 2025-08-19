from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

users = {}

class User(BaseModel):
    username: str
    password: str

@app.post("/users/")
async def create_user(user: User):
    if user.username not in users:
        users[user.username] = user.password
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")

@app.get("/users/")
async def get_users():
    return {"users": users}