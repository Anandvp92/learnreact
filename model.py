from database import Base,engine
from sqlalchemy import Column,Integer,String,DateTime
from pydantic import BaseModel
from typing import Optional
from datetime import date,datetime,time,timedelta


class ToDo(Base):
    __tablename__="Todos"
    id=Column(Integer,primary_key=True)
    task = Column(String(500),unique=True)
    created_date=Column(DateTime,default=datetime.utcnow)
    task_status=Column(Integer,default=0)


Base.metadata.create_all(engine)

class TodoRequest(BaseModel):
    task: str|None
    task_status: int 