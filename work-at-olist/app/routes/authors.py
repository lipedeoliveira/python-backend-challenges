from fastapi import  APIRouter
from app.database import Session
from app.models.authors import Author

router = APIRouter()

@router.get("/authors")
async def read_authors():
    session = Session()
    autores = session.query(Author).limit(20).all()
    resultado = [autores]
    session.close()
    return resultado