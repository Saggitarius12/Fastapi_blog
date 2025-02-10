from pydantic import BaseModel
from typing import Optional, List
# from pydantic.main import BaseConfig

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    class Config():
        from_attributes = True

class User(BaseModel):
    name: str
    email: str
    password: str
    is_admin: bool = False

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog] = []
    is_admin:bool = False

    class Config():
        from_attributes = True

class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config():
        from_attributes = True

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None