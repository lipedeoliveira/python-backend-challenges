from fastapi import FastAPI,APIRouter

app = FastAPI()

@app.get("/")
async def home():  
    return {"message":"Server working"}

@app.get("/authors")
async def authors():
    app.include_router(router)
    