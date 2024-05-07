from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

tasks = [
    Task(id=1, title="meow1", completed=False),
    Task(id=2, title="meow2", completed=True)
]

# Add new task
@app.post("/addTask")
async def addTask(task: Task):
    tasks.append(task)
    return task

# Get all tasks
@app.get("/getTasks", response_model=List[Task])
async def getAllTasks():
    return tasks

# Get task by id
@app.get("/getTask/{task_id}")
async def getTaskID(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Get task by name
@app.get("/getTask/{task_name}")
async def getTaskName(task_name: str):
    for task in tasks:
        if task.title == task_name:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# Delete all tasks
@app.delete("/delAllTasks")
async def delAllTasks():
    global tasks
    tasks = []
    return {"message": "All tasks deleted successfully"}

# Delete task by ID
@app.delete("/delTask/{task_id}")
async def delTaskID(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

# Delete task by name
@app.delete("/delTask/{task_name}")
async def delTaskTitle(task_name: str):
    for task in tasks:
        if task.title == task_name:
            tasks.remove(task)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

# Update task by ID
@app.put("/updateTask/{task_id}")
async def updateTask(task_id: int, updated_task: Task):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            tasks.append(updated_task)
            return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
