from pydantic import BaseModel, Field, EmailStr



class UserCreate(BaseModel):
    name: str= Field(min_length=2, max_length=50)
    age: int= Field(gt=0)
    email: EmailStr
    
class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    roles: list[str]

class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    age: int

class UserPatch(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    age: int | None = None


users = {
    1: {
        "id": 1,
        "name": "Alex",
        "email": "alex@example.com",
        "age": 30,
    }
}

