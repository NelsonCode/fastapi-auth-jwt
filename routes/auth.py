from fastapi import APIRouter, Header
from pydantic import BaseModel, EmailStr
from functions_jwt import validate_token, write_token
from fastapi.responses import JSONResponse

auth_routes = APIRouter()

class User(BaseModel):
    username: str
    email: EmailStr

@auth_routes.post("/login")
def login(user: User):
    print(user.dict())
    if user.username == "Nelson Hernandez":
        return write_token(user.dict())
    else:
        return JSONResponse(content={"message": "User not found"}, status_code=404)


@auth_routes.post("/verify/token")
def verify_token(Authorization: str = Header(None)):
    token = Authorization.split(" ")[1]
    return validate_token(token, output=True)
    