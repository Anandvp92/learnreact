import uvicorn
from views import app



if __name__=="__main__":   
    uvicorn.run("main:app",reload=True,port=4000)