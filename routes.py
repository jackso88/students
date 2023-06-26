from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import PostRemoveItem
import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/get")
async def get_posts(text: str, db: Session = Depends(get_db)):
    results_list = crud.search_post_by_text(db=db, search_text=text)
    return {"result": results_list}


@router.delete("/delete")
async def delete_posts(delete_id: PostRemoveItem,  db: Session = Depends(get_db)):
    result = crud.delete_by_id(db=db, id=delete_id.id)
    return {"result": result}

