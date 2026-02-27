
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task Manager API", version="1.0")

tasks = []
class Task(BaseModel):
    title: str
    description: str

@app.get("/")
def home():
    return {"message": "Task Manager API Running"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    task_data = task.dict()
    task_data["id"] = len(tasks)
    tasks.append(task_data)
    return {"message": "Task added", "task": task_data}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if task_id < len(tasks):
        deleted = tasks.pop(task_id)
        return {"message": "Task deleted", "task": deleted}
    return {"error": "Task not found"}