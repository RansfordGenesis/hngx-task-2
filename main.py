from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from database import models
from utils import crud
from schemas import schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app =FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    return crud.create_person(db=db, person=person)


@app.get("/api/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="person not found")
    return db_person