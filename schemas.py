from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    car_info_json: str  
    car_brand: str
    car_series_name: str
    car_year: str
    car_make: str
    car_fair_market_value: str
    car_sum_assured: str
    car_own_damage_theft: str
    car_excess_bodily_injury: str
    car_property_damage: str
    car_auto_personal_accident: str
    car_medical_reinbursment: str
    car_total_amount_due: str
    car_sum_assured_calculator: str
    car_excess_bodily_injury_manual: str
    car_your_rate: str    
    car_cptl: str
    car_premium: str
    car_doc_stamps: str
    car_vat: str
    car_local_government_tax: str
    car_cptl_val: str
    car_other_charges: str
    car_insurance_info_firstname: str
    car_insurance_info_lastname: str
    car_insurance_info_contact: str
    car_insurance_info_email: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    first_name: str    
    last_name: str    
    signup_phone: str    
    signup_country: str    
    signup_province_state: str    
    signup_city: str    
    signup_house_street: str    
    signup_zip_code: str    
    signup_license_no: str    
    signup_license_exp_date: str    
    signup_agent_refferor: str    
  

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True