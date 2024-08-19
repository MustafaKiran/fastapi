from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import BookingBase, BookingDisplay
from db.database import get_db
from db import db_booking

router = APIRouter(
    prefix='/bookings',
    tags=['bookings']
)

@router.post('/', response_model=BookingDisplay)
def create_booking(request: BookingBase, db: Session = Depends(get_db)):
    return db_booking.create_booking(db, request)

@router.get('/{id}', response_model=BookingDisplay)
def read_booking(id: int, db: Session = Depends(get_db)):
    booking = db_booking.get_booking(db, id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.get('/', response_model=list[BookingDisplay])
def get_all_bookings(db: Session = Depends(get_db)):
    return db_booking.get_all_bookings(db)

@router.delete('/{id}', response_model=dict)
def delete_booking(id: int, db: Session = Depends(get_db)):
    booking = db_booking.delete_booking(db, id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return {"message": "Booking deleted"}
