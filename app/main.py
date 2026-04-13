from fastapi import FastAPI
from app.database.database import Base, engine
from app.routes import user

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user.router)

@app.get("/")
def home():
    return {"message": "Secure API is running"}
