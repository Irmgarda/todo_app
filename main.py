from fastapi import FastAPI
from .database import engine, Base
from .routers import todo, auth

# Initialize database tables
Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Include the routers for different functionalities
app.include_router(todo.router)
app.include_router(auth.router)
