from database import Base,engine
from sqlalchemy import Column,Integer,String

class ToDo(Base):
    __tablename__="Todos"
    id=Column(Integer,primary_key=True)
    task = Column(String(500))


Base.metadata.create_all(engine)

