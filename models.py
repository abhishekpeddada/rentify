from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    email = Column(String(120), unique=True)
    password = Column(String(120))
    phone_number = Column(String(15))
    user_type = Column(String(10))  # 'seller' or 'buyer'

    def __init__(self, first_name=None, last_name=None, email=None,password=None, phone_number=None, user_type=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.user_type = user_type

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True)
    email = Column(String(120))
    place = Column(String(100))
    area = Column(String(100))
    bedrooms = Column(Integer)
    bathrooms = Column(Integer)
    nearby_hospitals = Column(String(200))
    nearby_colleges = Column(String(200))
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    def __init__(self, email = None,place=None, area=None, bedrooms=None, bathrooms=None, nearby_hospitals=None, nearby_colleges=None, user_id=None):
        self.email = email
        self.place = place
        self.area = area
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.nearby_hospitals = nearby_hospitals
        self.nearby_colleges = nearby_colleges
        self.user_id = user_id
