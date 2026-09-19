from fastapi import FastAPI, HTTPException
from apitest.user import UserCreate, UserResponse, UserUpdate, UserPatch, users



app = FastAPI()


@app.get("/health")
def get_health():
    return {"status": "ok"}


@app.get("/hello/{name}")
def print_hello_name(name: str):
    return {"message": f"Hello {name}"}



@app.get("/users")
def get_users(limit: int):
    return {"limit": limit} 


@app.post("/users", response_model=UserResponse)
def create_user(user: UserCreate):
    return {
        "id": 1,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "roles": list[str]
    }

@app.put("/users/{id}", response_model=UserResponse)
def update_user(user_id, user: UserUpdate):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")

    users[user_id] = {
        "id": user_id,
        **user.model_dump(),
    }
    return users[user_id]


@app.patch("/users/{user_id}", response_model=UserResponse)
def patch_user(user_id: int, user: UserPatch):
    if user_id not in users: 
        raise HTTPException(status_code=404, detail="user not found")
    update_data = user.model_dump(exclude_unset=True)
    users[user_id].update(update_data)

    return users[user_id]

@app.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: int):
    if not user_id in users:
        raise HTTPException(status_code=404, detail="user not found")

    del users[user_id]
    
@app.get("/version")
def get_version():
    return{"version":"1.0"}

@app.get("/status")
def get_status():
    return {"status": "running"}


@app.get("/info")
def get_info():
    return {
        "service": "user-api",
        "version": "1.0"
    }


@app.get("/ping")
def ping():
    return {"message": "pong"}

