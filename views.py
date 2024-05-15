from fastapi import FastAPI,HTTPException,Depends
from model import ToDo
from sqlalchemy.orm import Session
from database import engine
from fastapi import status
from model import TodoRequest
from datetime import datetime

session = Session(autocommit=False,autoflush=False,bind=engine)

app = FastAPI(debug=True)



@app.get("/")
async def home():
    return {"hello world"}


@app.get("/list/{id}")
async def list_todo(id:int):
    with session as  SessIon:
        todo_task=SessIon.query(ToDo).get(id)
        if not todo_task:
           raise HTTPException(status_code=404,detail=f"No task found in this id:{id}")
    return {"id":todo_task.id,"Task":todo_task.task}  
      

@app.get("/listall/")
async def list_all_task():
   with session as SessIon:
      result=SessIon.query(ToDo).all()
      if not result:
         raise HTTPException(status_code=404,detail="No task's found")
         
      return ({"id":i.id,"task":i.task,"created time":i.created_date ,"status":i.task_status,"updated date":i.updated_date} for i in result)

@app.post("/create/",status_code=status.HTTP_200_OK)
async def create_todo(todo:TodoRequest):    
    tododb=ToDo(task=todo.task)
    with session as SessIon:
        SessIon.add(tododb)
        session.commit()
        return {"message":f"create todo {tododb.id}"}



@app.put("/updatetodo/{id}")
async def update_todo(id:int,item:TodoRequest):

    with session as SessIon:      
        existing_item= session.query(ToDo).filter(ToDo.id==id).first()
        if existing_item:
            existing_item.task_status=item.task_status
            existing_item.task=item.task
            existing_item.updated_date=datetime.now()
            SessIon.commit()
            SessIon.refresh(existing_item)
            return {"message":f"Todo in id {existing_item.id} is updated"}
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



