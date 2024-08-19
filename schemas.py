from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import List


class UserBase(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserDisplay(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class HotelBase(BaseModel):
    name: str
    description: str
    # star_rating: float
    # phone_number: str
    # address: str
    # city: str
    # state: str
    # country: str
    # zip_code: str
    # latitude: float
    # longitude: float
    # number_of_rooms: int
    # room_types: str
    # price_per_night: float

class HotelDisplay(BaseModel):
    id: int
    name: str
    description: str
    # star_rating: float
    # phone_number: str
    # address: str
    # city: str
    # state: str
    # country: str
    # zip_code: str
    # latitude: float
    # longitude: float
    # number_of_rooms: int
    # room_types: str
    # price_per_night: float

    class Config:
        from_attributes = True

# Booking Schemas
class BookingBase(BaseModel):
    user_id: int
    hotel_id: int
    start_date: datetime
    end_date: datetime

class BookingDisplay(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    start_date: datetime
    end_date: datetime

    class Config:
        from_attributes = True
