from sqladmin import Admin, ModelView
from database.config import engine,SessionLocal
from models.models import User,Blog  
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from schema.hash import Hash

class AdminAuth(AuthenticationBackend):
    async def login(self,request:Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")
        session = SessionLocal()
        user = session.query(User).filter(User.email == username).first()
        if user and Hash.verify(user.password,password):
            if user.is_admin:
                request.session.update({"token":user.email})
                return True
        else:
            return False
    async def logout(self,request:Request)-> bool:
        request.session.clear()
        return True
    
    async def authenticate(self,request:Request)-> bool:
        token = request.session.get("token")
        return token is not None
    

class UserAdmin(ModelView, model=User):
        
        column_list = [
            'id', 'name', 'email', 'password', 'blogs','is_admin'
        ]

class BlogView(ModelView,model=Blog):
    column_list = [
        'id', 'title', 'body', 'user_id','creator'
    ]


def create_admin(app):
    authentication_backend = AdminAuth(secret_key="supersecretkey")
    admin = Admin(app=app, engine=engine, authentication_backend=authentication_backend)
    admin.add_view(UserAdmin)
    admin.add_view(BlogView)
    
    return admin

