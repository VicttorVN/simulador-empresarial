
from fastapi import FastAPI
from backend.database import engine, Base
from backend import models, simulador_logic

app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
