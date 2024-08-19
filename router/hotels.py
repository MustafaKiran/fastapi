from typing import List
from schemas import HotelBase, HotelDisplay, UserBase
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_hotel


router = APIRouter(
  prefix='/hotel',
  tags=['hotel']
)

# Create hotel
@router.post('/', response_model=HotelDisplay)
def create_hotel(request: HotelBase, db: Session = Depends(get_db)):
  return db_hotel.create_hotel(db, request)

# Get specific hotel
@router.get('/{id}', response_model=HotelDisplay)
def get_hotel(id: int, db: Session = Depends(get_db)):
  return {
    'data': db_hotel.get_hotel(db, id)
  }

# Read all hotels
@router.get('/', response_model=List[HotelDisplay])
def get_all_hotel(db: Session = Depends(get_db)):
  return db_hotel.get_all_hotel(db)

# Update hotel
@router.put('/{id}/update')
def update_hotel(id: int, request: HotelBase, db: Session = Depends(get_db)):
  return db_hotel.update_hotel(db, id, request)

# Delete hotel
@router.delete('/delete/{id}')
def delete(id: int, db: Session = Depends(get_db)):
  return db_hotel.delete_hotel(db, id)