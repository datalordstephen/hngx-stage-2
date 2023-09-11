from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from pydantic import BaseModel
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

# create all tables in the db
models.Base.metadata.create_all(bind=engine)

class Person(BaseModel):
    name: str
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/api")
def add_person(payload: Person, db: db_dependency):
    db_person = models.Person(name = payload.name)
    db.add(db_person)
    db.commit()

@app.get("/api/{id}")
def get_person(id: int, db: db_dependency):
    res = db.query(models.Person).filter(models.Person.id == id).first()
    if not res:
        raise HTTPException(status_code=404, detail="Person not found")
    return res

@app.put("/api/{id}")
def update_person(id: int, db: db_dependency, payload: Person):
    db.query(models.Person).filter(models.Person.id == id).update({"name": payload.name}, synchronize_session=False)
    db.commit()
    raise HTTPException(status_code=200, detail="Person updated")
    

@app.delete("/api/{id}")
def delete_person(id: int, db: db_dependency):
    db.query(models.Person).filter(models.Person.id == id).delete(synchronize_session=False)
    db.commit()
    raise HTTPException(status_code=204, detail="Person deleted")