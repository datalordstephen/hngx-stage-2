from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
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

# overwriting the default error message for validation errors on pydantic model
@app.exception_handler(RequestValidationError)
async def validator_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid request body"}
    )

@app.post("/api", status_code=201)
def add_person(payload: Person, db: db_dependency):
    res = db.query(models.PersonClass).filter(models.PersonClass.name == payload.name).first()
    if res is not None:
        raise HTTPException(status_code=400, detail="Person already exists")
    
    db_person = models.PersonClass(name = payload.name)
    db.add(db_person)
    db.commit()
    
    return {"id": db_person.id, "name": db_person.name}

@app.get("/api/{id}")
def get_person(id: int, db: db_dependency, payload: Person | None = None):
    if payload is None:
        res = db.query(models.PersonClass).filter(models.PersonClass.id == id).first()
    else:
        res = db.query(models.PersonClass).filter(models.PersonClass.name == payload.name).first()
    if not res:
        raise HTTPException(status_code=404, detail="Person not found")
    
    return res

@app.put("/api/{id}")
def update_person(id: int, db: db_dependency, payload: Person | None = None):
    res = db.query(models.PersonClass).filter(models.PersonClass.id == id).first()
    
    if res is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    db.query(models.PersonClass).filter(models.PersonClass.id == id).update({"name": payload.name}, synchronize_session=False)
    db.commit()
    db.refresh(res)

    return {"id": id, "name": payload.name}
    

@app.delete("/api/{id}", status_code=204)
def delete_person(id: int, db: db_dependency, payload: Person | None = None):
    is_payload_none = payload is None
    if is_payload_none:
        res = db.query(models.PersonClass).filter(models.PersonClass.id == id).first()
    else:
        res = db.query(models.PersonClass).filter(models.PersonClass.name == payload.name).first()
        
    if res is None:
        raise HTTPException(status_code=404, detail="Person not found")
    
    if is_payload_none:
        db.query(models.PersonClass).filter(models.PersonClass.id == id).delete(synchronize_session=False)
    else:
        db.query(models.PersonClass).filter(models.PersonClass.name == payload.name).delete(synchronize_session=False)
        
    db.commit()