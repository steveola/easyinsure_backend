from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

#from . import Base
import database
Base= database.Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    signup_phone = Column(String, index=True)
    signup_country = Column(String, index=True)
    signup_province_state = Column(String, index=True)
    signup_city = Column(String, index=True)
    signup_house_street = Column(String, index=True)
    signup_zip_code = Column(String, index=True)
    signup_license_no = Column(String, index=True)
    signup_license_exp_date = Column(String, index=True)
    signup_agent_refferor = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    car_info_json = Column(String, index=True)
    car_brand = Column(String, index=True)
    car_series_name = Column(String, index=True)
    car_year = Column(String, index=True)
    car_make = Column(String, index=True)
    car_fair_market_value = Column(String, index=True)
    car_sum_assured = Column(String, index=True)
    car_own_damage_theft = Column(String, index=True)
    car_excess_bodily_injury = Column(String, index=True)
    car_excess_bodily_injury = Column(String, index=True)
    car_property_damage = Column(String, index=True)
    car_auto_personal_accident = Column(String, index=True)
    car_medical_reinbursment = Column(String, index=True)
    car_total_amount_due = Column(String, index=True)
    car_sum_assured_calculator = Column(String, index=True)
    car_excess_bodily_injury_manual = Column(String, index=True)
    car_your_rate = Column(String, index=True)
    car_cptl = Column(String, index=True)
    car_premium = Column(String, index=True)
    car_doc_stamps = Column(String, index=True)
    car_vat = Column(String, index=True)
    car_local_government_tax = Column(String, index=True)
    car_cptl_val = Column(String, index=True)
    car_other_charges = Column(String, index=True)
    car_insurance_info_firstname = Column(String, index=True)
    car_insurance_info_lastname = Column(String, index=True)
    car_insurance_info_contact = Column(String, index=True)
    car_insurance_info_email = Column(String, index=True)

    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")