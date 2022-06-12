from cgitb import strong
from tokenize import String
from sqlalchemy.orm import Session

#from . import models, schemas
import models
import schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_current_user(db: Session, user_cookie: str):
    user_id = int(user_cookie.split("-")[1])
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_auth_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(models.User.email == email).filter(models.User.hashed_password == (password  + "notreallyhashed")).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email,
            first_name=user.first_name,
            last_name=user.last_name,
            signup_phone=user.signup_phone, 
            signup_country=user.signup_country, 
            signup_province_state=user.signup_province_state, 
            signup_city=user.signup_city, 
            signup_house_street=user.signup_house_street, 
            signup_zip_code=user.signup_zip_code, 
            signup_license_no=user.signup_license_no, 
            signup_license_exp_date=user.signup_license_exp_date, 
            signup_agent_refferor=user.signup_agent_refferor, 
            hashed_password=fake_hashed_password
        )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    uid = db_user.id;
    suid = str(uid)
    #return {"cookie": "fluttercookie" + "-" + suid, "" : "Succesful Registration!"}


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(),
                    owner_id=user_id
                )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_houses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.House).offset(skip).limit(limit).all()

def create_user_house(db: Session, house: schemas.HouseCreate, user_id: int):
    db_house = models.House(**house.dict(),
                    owner_id=user_id
                )
    db.add(db_house)
    db.commit()
    db.refresh(db_house)
    return db_house

       
def get_condos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Condo).offset(skip).limit(limit).all()

def create_user_condo(db: Session, condo: schemas.CondoCreate, user_id: int):
    db_condo = models.Condo(**condo.dict(),
                    owner_id=user_id
                )
    db.add(db_condo)
    db.commit()
    db.refresh(db_condo)
    return db_condo