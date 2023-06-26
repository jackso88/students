import uvicorn
from fastapi import FastAPI
import models
from routes import router
from config import engine
import converter
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/posts.csv", tags=["Document search engine"])
converter.main()

