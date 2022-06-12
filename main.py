from typing import List
from tokenize import String
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

#from . import crud, models, schemas
import crud
import models
import schemas
#from .database import SessionLocal, engine
import database
SessionLocal= database.SessionLocal
engine= database.engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Welcome": "Easy Insure API"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/generate_auth_cookie/{email}/{password}", response_model=schemas.User)
def read_user(email: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_auth_user(db, email=email, password=password)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/get_currentuserinfo/{user_cookie}", response_model=schemas.User)
def read_user(user_cookie: str, db: Session = Depends(get_db)):
    db_user = crud.get_current_user(db, user_cookie=user_cookie)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)

@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items

@app.post("/users/{user_id}/houses/", response_model=schemas.House)
def create_house_for_user(
    user_id: int, house: schemas.HouseCreate, db: Session = Depends(get_db)
):
    return crud.create_user_house(db=db, house=house, user_id=user_id)


@app.get("/houses/", response_model=List[schemas.House])
def read_houses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    houses = crud.get_houses(db, skip=skip, limit=limit)
    return houses

@app.post("/users/{user_id}/condos/", response_model=schemas.Condo)
def create_condo_for_user(
    user_id: int, condo: schemas.CondoCreate, db: Session = Depends(get_db)
):
    return crud.create_user_condo(db=db, condo=condo, user_id=user_id)


@app.get("/condos/", response_model=List[schemas.Condo])
def read_condos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    condos = crud.get_condos(db, skip=skip, limit=limit)
    return condos