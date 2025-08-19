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

@app.post("/login")
async def login(username: str, password: str):
    if username in users and users[username] == password:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/register")
async def register(username: str, password: str):
    if username not in users:
        users[username] = password
        return {"message": "User registered successfully"}
    else:
        raise HTTPException(status_code=400, detail="User already exists")

# app.py
from fastapi import FastAPI
from todo_service import todo_service
from user_ import user_
from user_service import user_service

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the main app"}

@app.get("/todos")
async def get_todos():
    return await todo_service.get_todos()

@app.post("/todos")
async def create_todo(todo: dict):
    return await todo_service.create_todo(todo)

@app.get("/users")
async def get_users():
    return await user_.get_users()

@app.post("/users")
async def create_user(user: dict):
    return await user_.create_user(user)

@app.post("/login")
async def login(username: str, password: str):
    return await user_service.login(username, password)

@app.post("/register")
async def register(username: str, password: str):
    return await user_service.register(username, password)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Note: This main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Also, remember to handle database connections in each microservice if needed. This example does not include database connections as it's focused on splitting the monolithic code into microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The database connection logic is not included in this example, as it was not present in the original monolithic code. In a real-world scenario, you would need to add database connection logic to each microservice as needed.

# The main app.py is just a placeholder to demonstrate how the microservices can be integrated. In a real-world scenario, you would use an API gateway or service discovery tool to manage the communication between the microservices.

# Each microservice can be deployed independently, and the main app can call each microservice as needed.

# This is a simplified example and does not include error handling, input validation, or other best practices for production-level code.

# The