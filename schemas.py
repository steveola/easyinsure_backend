from typing import List, Optional

from pydantic import BaseModel


class HouseBase(BaseModel):
    title: str
    house_info_json: str  
    description: Optional[str] = None
    doc_stamps: Optional[str] = None
    fire_service_stamps: Optional[str] = None
    house_external_walls_entirely_concrete: Optional[str] = None
    house_located_inside_village_subdivision: Optional[str] = None
    house_no_building_amount: Optional[str] = None
    house_no_city: Optional[str] = None
    house_no_construction: Optional[str] = None
    house_no_construction_other: Optional[str] = None
    house_no_contents_amount: Optional[str] = None
    house_no_country: Optional[str] = None
    house_no_firefighting_mitigating_measure_equipment: Optional[str] = None
    house_no_house_street: Optional[str] = None
    house_no_items_to_insure: Optional[str] = None
    house_no_number_of_stories: Optional[str] = None
    house_no_perils_covered_aon: Optional[str] = None
    house_no_perils_covered_auto_personal_accident: Optional[str] = None
    house_no_perils_covered_own_damage_theft: Optional[str] = None
    house_no_perils_excess_bodily_injury: Optional[str] = None
    house_no_perils_medical_reimbursement: Optional[str] = None
    house_no_perils_property_damage: Optional[str] = None
    house_no_province: Optional[str] = None
    house_no_province_state: Optional[str] = None
    house_no_residential_home_package_options: Optional[str] = None
    house_no_zip_code: Optional[str] = None
    house_used_entirely_as_residence: Optional[str] = None
    house_yes_city: Optional[str] = None
    house_yes_country: Optional[str] = None
    house_yes_email: Optional[str] = None
    house_yes_house_street: Optional[str] = None
    house_yes_last_name: Optional[str] = None
    house_yes_name: Optional[str] = None
    house_yes_phone: Optional[str] = None
    house_yes_province_state: Optional[str] = None
    house_yes_zip_code: Optional[str] = None
    vat: Optional[str] = None
    local_govt_tax: Optional[str] = None
    premium: Optional[str] = None
    sum_assured: Optional[str] = None
    total_amount_due: Optional[str] = None

class HouseCreate(HouseBase):
    pass


class House(HouseBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#END HOUSE

class CondoBase(BaseModel):
    title: str
    condo_info_json: str  
    description: Optional[str] = None
    condo_external_walls_entirely_concrete: Optional[str] = None
    condo_no_boundaries: Optional[str] = None
    condo_no_building_amount: Optional[str] = None
    condo_no_city: Optional[str] = None
    condo_no_construction: Optional[str] = None
    condo_no_contents_amount: Optional[str] = None
    condo_no_country: Optional[str] = None
    condo_no_firefighting_mitigating_measure_equipment: Optional[str] = None
    condo_no_items_to_insure: Optional[str] = None
    condo_no_number_of_stories: Optional[str] = None
    condo_no_perils_covered_aon: Optional[str] = None
    condo_no_perils_covered_auto_personal_accident: Optional[str] = None
    condo_no_perils_covered_own_damage_theft: Optional[str] = None
    condo_no_perils_excess_bodily_injury: Optional[str] = None
    condo_no_perils_medical_reimbursement: Optional[str] = None
    condo_no_perils_property_damage: Optional[str] = None
    condo_no_province_state: Optional[str] = None
    condo_no_roofing: Optional[str] = None
    condo_no_roofing_others: Optional[str] = None
    condo_no_zip_code: Optional[str] = None
    condo_yes_city: Optional[str] = None
    condo_yes_condo_street: Optional[str] = None
    condo_yes_country: Optional[str] = None
    condo_yes_email: Optional[str] = None
    condo_yes_name: Optional[str] = None
    condo_yes_no_occupancy: Optional[str] = None
    condo_yes_phone: Optional[str] = None
    condo_yes_province_state: Optional[str] = None
    condo_yes_residential_home_package_option: Optional[str] = None
    condo_yes_zip_code: Optional[str] = None
    doc_stamps: Optional[str] = None
    fire_service_stamps: Optional[str] = None
    vat: Optional[str] = None
    local_govt_tax: Optional[str] = None
    premium: Optional[str] = None
    sum_assured: Optional[str] = None
    total_amount_due: Optional[str] = None

class CondoCreate(CondoBase):
    pass


class Condo(CondoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

#END CONDO

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

#END ITEM

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
    houses: List[House] = []
    condos: List[Condo] = []

    class Config:
        orm_mode = True