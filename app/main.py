from fastapi import FastAPI
from app.database.database import Base, engine
from app.models import user

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Secure API is running"}
