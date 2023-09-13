from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from database import models
from utils import crud
from schemas import schemas
from database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)


app =FastAPI()

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:63342",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api", response_model=schemas.Person)
def create_person(person: schemas.PersonCreate, db: Session = Depends(get_db)):
    if not person.name:
        raise HTTPException(status_code=400, detail="Name is required")
    return crud.create_person(db=db, person=person)


@app.get("/api/{person_id}", response_model=schemas.Person)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="person not found")
    return db_person


@app.put("/api/{person_id}", response_model=schemas.Person)
def update_person(person_id: int, updated_person: schemas.PersonBase, 
        db: Session = Depends(get_db)):
    
    db_person = crud.get_person(db, person_id=person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    updated_person_dict = updated_person.dict(exclude_unset=True)
    for field, value in updated_person_dict.items():
        setattr(db_person, field, value)

    db.commit()
    db.refresh(db_person)
    return db_person


@app.delete("/api/{person_id}", response_model=dict)
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = crud.get_person(db, person_id=person_id)
    
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")

    db.delete(db_person)
    db.commit()

    return {"message": "Person deleted successfully"}
