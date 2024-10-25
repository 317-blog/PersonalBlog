from pydantic import BaseModel, Field, EmailStr
from typing_extensions import Annotated, List


class User(BaseModel):
    name: str
    user_email: EmailStr = Field(pattern='^[a-zA-Z0-9_.+-]+@+[a-zA-Z0-9_.+-]+\\.[a-zA-Z]{2,}$', example='<EMAIL>')
    password: str
    article: List[int]
