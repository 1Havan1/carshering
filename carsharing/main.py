from app import app, Base, engine
import uvicorn

if __name__=='__main__':
    Base.metadata.create_all(engine)
    uvicorn.run("main:app", port=8080, host='localhost', reload=True)