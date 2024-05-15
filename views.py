from fastapi import FastAPI,HTTPException,Depends
from model import ToDo
from sqlalchemy.orm import Session
from database import engine
from fastapi import status
from model import TodoRequest

session= Session(autocommit=False,autoflush=False,bind=engine,expire_on_commit=False)

app = FastAPI(debug=True)



@app.get("/")
async def home():
    return {"hello world"}


@app.get("/list/{id}")
async def list_todo(id:int):
    with session as  SessIon:
        todo_task=SessIon.query(ToDo).get(id)
    return {f"todo item with id:{todo_task.id}":f"and the task {todo_task.task}"}        

@app.get("/singletodo/{id}")
async def single_todo(id:int):
    return {"single todo {id}"}

@app.post("/create/",status_code=status.HTTP_200_OK)
async def create_todo(todo:TodoRequest):    
    tododb=ToDo(task=todo.task)
    with session as SessIon:
        SessIon.add(tododb)
        session.commit()
        return {"message":f"create todo {tododb.id}"}

@app.put("/updatetodo/{id}",response_model=TodoRequest)
async def update_todo(id:int,todo:TodoRequest):
    with session as SessIon:
        result= SessIon.query(ToDo).filter(ToDo.id==id).first()
        if result:
            return {"task":f"{result.id}"}
        else:
            raise HTTPException(status_code=404,detail="Task not found")
  
   
        
        
        
@app.delete("/deletetodo/{id}")
async def delete_todo(id:int):
    with session as sessIon:
       result= sessIon.query(ToDo).get(id)
       if result:
        sessIon.delete(result)
        sessIon.commit()
        return {"message":f" Task is deleted {result.task}"}
       else:
        return {"result todo not found in id: {id}"}



