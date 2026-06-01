from fastapi import APIRouter, HTTPException
from api.database import SessionLocal
from api.models.todo import Todo
from api.schemas.todo import PostTodo, PutTodo

todo_router = APIRouter(prefix="/api", tags=["Todo"])

@todo_router.get("/")
def all_todos():
    
    db = SessionLocal()
    todos = db.query(Todo).all()
    db.close()

    return todos


@todo_router.post("/")
def post_todo(todo: PostTodo):
    
    db = SessionLocal()

    new_todo = Todo(
        task =todo.task,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    db.close()

    return new_todo

@todo_router.put("/{todo_id}")
def update_todo(todo_id: int, todo: PutTodo):
    
    db = SessionLocal()

    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if existing_todo is None:
        db.close()
        raise HTTPException(status_code=404, detail="Todo not found")
    
    if todo.task is not None:
        existing_todo.task = todo.task

    if todo.completed is not None:
        existing_todo.completed = todo.completed

    db.commit()
    db.refresh(existing_todo)

    db.close()

    return existing_todo

@todo_router.delete("/{todo_id}")
def delete_todo(todo_id: int):
    
    db = SessionLocal()
    
    existing_todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if existing_todo is None:
        db.close()
        raise HTTPException(status_code=404, detail="Todo not found")
    

    db.delete(existing_todo)
    db.commit()

    db.close()

    return {"message": "Todo deleted successfully"}