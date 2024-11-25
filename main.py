from fastapi import FastAPI, HTTPException, Depends, Request
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize FastAPI application
app = FastAPI()

######################## API Token from .env
ACCESS_TOKEN = os.getenv("API_TOKEN")

######################## Dependency for Token Authentication
def authenticate_request(request: Request):
    token = request.headers.get("GOODJOB")
    if token != f"Bearer {ACCESS_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized access")
    return token


######################## Data Storage for API versions
tasks_data_v1 = [
    {"id": 1, "title": "Learn FastAPI", "description": "Start with the basics of FastAPI.", "completed": False}
]

tasks_data_v2 = [
    {"id": 1, "title": "Enhance To-Do API", "description": "Add advanced features to API.", "completed": False}
]


######################## API v1 Endpoints
@app.get("/api/v1/tasks/{task_id}")
def fetch_task_by_id_v1(task_id: int):
    task = next((item for item in tasks_data_v1 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "data": task}


@app.post("/api/v1/tasks/", status_code=201)
def create_task_v1(title: str, description: str):
    new_task = {"id": len(tasks_data_v1) + 1, "title": title, "description": description, "completed": False}
    tasks_data_v1.append(new_task)
    return {"status": "success", "data": new_task}


@app.delete("/api/v1/tasks/{task_id}", status_code=204)
def remove_task_v1(task_id: int):
    task = next((item for item in tasks_data_v1 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_data_v1.remove(task)
    return {"status": "success", "message": "Task removed successfully"}


@app.patch("/api/v1/tasks/{task_id}", status_code=204)
def modify_task_v1(task_id: int, title: str = None, description: str = None, completed: bool = None):
    task = next((item for item in tasks_data_v1 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if title:
        task["title"] = title
    if description:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed
    return {"status": "success", "data": task}


######################## API v2 Endpoints
@app.get("/api/v2/tasks/{task_id}")
def fetch_task_by_id_v2(task_id: int):
    task = next((item for item in tasks_data_v2 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"status": "success", "data": task}


@app.post("/api/v2/tasks/", status_code=201)
def create_task_v2(title: str, description: str):
    new_task = {"id": len(tasks_data_v2) + 1, "title": title, "description": description, "completed": False}
    tasks_data_v2.append(new_task)
    return {"status": "success", "data": new_task}


@app.delete("/api/v2/tasks/{task_id}", status_code=204)
def remove_task_v2(task_id: int):
    task = next((item for item in tasks_data_v2 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks_data_v2.remove(task)
    return {"status": "success", "message": "Task removed successfully"}


@app.patch("/api/v2/tasks/{task_id}", status_code=204)
def modify_task_v2(task_id: int, title: str = None, description: str = None, completed: bool = None):
    task = next((item for item in tasks_data_v2 if item["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if title:
        task["title"] = title
    if description:
        task["description"] = description
    if completed is not None:
        task["completed"] = completed
    return {"status": "success", "data": task}
