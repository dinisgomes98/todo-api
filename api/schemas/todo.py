from pydantic import BaseModel, Field
from typing import Optional

class TodoResponse(BaseModel):
    id: int
    task: str
    completed: bool

    class Config:
        from_attributes = True

class PostTodo(BaseModel):
    task: str = Field(..., max_length=100)
    completed: bool

class PutTodo(BaseModel):
    task: Optional[str] = Field(None, max_length=100)
    completed: Optional[bool]

    