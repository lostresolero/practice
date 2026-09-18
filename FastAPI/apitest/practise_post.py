@app.post("/users", status_code=201)
def create_user(user: UserCreate):
    if any(existing_user["emai"] in users.values()):
        raise HTTPException(status_code=409, detail="email already exists")

    user_id = max(user.keys(), default=0) +1


    user[user_id]= {
        "id" : user_id,
        **user.model_dump()
    }    


    returns users[user_id]    