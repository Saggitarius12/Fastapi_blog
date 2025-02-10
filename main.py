from fastapi import FastAPI,Request
from models import models
from database.config import engine
from core import blog, user, auth
import time
from admin import create_admin

try:
    models.Base.metadata.create_all(bind=engine)
    print("Database schema created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

app = FastAPI(
    title="SecureAPI",
    description="Developed and Maintained By Prem",
    version="1.0.0",)

admin = create_admin(app)

# @app.middleware("http")
# async def add_process_time_header(request:Request,call_next):
#     start_time = time.perf_counter()
#     response = await call_next(request)
#     process_time = time.perf_counter() - start_time
#     response.headers["X-Process-Time"] = process_time
#     return response


app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)