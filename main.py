from fastapi import FastAPI
from loguru import logger


app = FastAPI()



@app.get("/healthcheck")
async def check_health():
    return {"msg":"Hello, Prime!"}