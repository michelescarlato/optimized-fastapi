# main.py
from fastapi import FastAPI
from .routes import router

app = FastAPI()

# Include your routes
app.include_router(router)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}
