from fastapi import FastAPI,status
import uvicorn
from model import ToDo
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine

class TodoRequest(BaseModel):
    task:str


app = FastAPI(debug=True)

@app.get("/list/")
async def list_todo():
    return {"list todo"}

@app.get("/singletodo/{id}")
async def single_todo(id:int):
    return {"single todo {id}"}

@app.post("/create/",status_code=status.HTTP_200_OK)
async def create_todo(todo:TodoRequest):
    session= Session(bind=engine,expire_on_commit=False)
    tododb=ToDo(task=todo.task)
    session.add(tododb)
    session.commit()
    id=tododb.id
    session.close()
    return {"message":"create todo {id}"}

@app.put("/updatetodo/{id}")
async def update_todo(id:int):
    return {"update todo {id}"}

@app.delete("/deletetodo/{id}")
async def delete_todo(id:int):
    return {"delete todo {id}"}




if __name__=="__main__":
   
    uvicorn.run("backend:app",reload=True,port=3000)