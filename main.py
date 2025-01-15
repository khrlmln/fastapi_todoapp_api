from fastapi import FastAPI
from starlette import status

from database import engine
from models import Base
from routers import admin, auth, todos, users

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/healthy", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "API is running"}


app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(todos.router)
