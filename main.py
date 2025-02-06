from fastapi import FastAPI
from models import models
from database.config import engine
from core import blog, user, auth

try:
    models.Base.metadata.create_all(bind=engine)
    print("Database schema created successfully.")
except Exception as e:
    print(f"An error occurred: {e}")

app = FastAPI(
    title="SecureAPI",
    description="Developed and Maintained By Prem",
    version="1.0.0",)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)