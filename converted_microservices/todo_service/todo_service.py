from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

todos = []

class Todo(BaseModel):
    todo: str

@app.post("/todos/")
async def create_todo(todo: Todo):
    todos.append(todo.todo)
    return {"message": "Todo added successfully"}

@app.get("/todos/")
async def get_todos():
    return {"todos": todos}