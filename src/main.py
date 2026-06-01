from fastapi import FastAPI
from api.routes.todo import todo_router
from api.database import Base, engine
from api.models.todo import Todo

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(todo_router)


@app.get("/")
def index():
    return {"status": "todo api is running"}