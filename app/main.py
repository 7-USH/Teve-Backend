from fastapi import FastAPI
from teve.routers import user,login, fav
from teve.models import models
import uvicorn
from teve.database.database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(login.router)
app.include_router(user.router)
app.include_router(fav.router)

if __name__ == '__main__':
    uvicorn.run("main:app",host="0.0.0.0",port=8080,reload=True)