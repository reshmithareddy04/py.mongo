# routes/user.py
from fastapi import APIRouter
from models.user import User 
from config.db import conn 
from schemas.user import serializeDict, serializeList
from bson import ObjectId

user = APIRouter()

# Route to find all users
@user.get('/')
async def find_all_users():
    return serializeList(conn.local.user.find())

# Route to create a new user
@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

# Route to update an existing user by ID
@user.put('/{id}')
async def update_user(id: str, user: User):
    conn.local.user.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id": ObjectId(id)}))

# Route to delete a user by ID
@user.delete('/{id}')
async def delete_user(id: str):
    return serializeDict(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
