# index.py
from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user, prefix="/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
