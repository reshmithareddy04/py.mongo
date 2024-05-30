# models/user.py
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    age: int
