# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# import uvicorn
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # Startup code
#     print("App starting...")
#
#     yield  # פה האפליקציה רצה
#
#     # Shutdown code
#     print("App stopping...")
#
#
# app = FastAPI(lifespan=lifespan)
#
#
# @app.get("/ddd")
# def read_root():
#     return {"Hello": "World"}
#
# if __name__ == "__main__":
#
#     uvicorn.run("lifespan:app", host="127.0.0.1", port=8000, reload=True)
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from contextlib import asynccontextmanager

# Lifespan – Startup / Shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App starting...")  # Startup
    yield                      # השרת רץ כאן
    print("App stopping...")   # Shutdown

app = FastAPI(lifespan=lifespan)

# BaseModel ל-User
class User(BaseModel):
    id: int
    name: str
    age: int

# "Database" בזיכרון
db: List[User] = []

# ======= CRUD =======

# CREATE
@app.post("/users/", response_model=User)
def create_user(user: User):
    db.append(user)
    return user

# READ ALL
@app.get("/users/", response_model=List[User])
def get_users():
    return db

# READ ONE
@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    for user in db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

# UPDATE
@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, updated_user: User):
    for i, user in enumerate(db):
        if user.id == user_id:
            db[i] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(db):
        if user.id == user_id:
            db.pop(i)
            return {"detail": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

# ======= להרצה מקומית =======
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("lifespan:app", host="127.0.0.1", port=8000, reload=True)
