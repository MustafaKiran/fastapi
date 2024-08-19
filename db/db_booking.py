from sqlalchemy.orm import Session
from db.models import DbBooking
from schemas import BookingBase


def create_booking(db: Session, request: BookingBase):
    new_booking = DbBooking(
        user_id=request.user_id,
        hotel_id=request.hotel_id,
        start_date=request.start_date,
        end_date=request.end_date
    )
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking


def get_booking(db: Session, id: int):
    return db.query(DbBooking).filter(DbBooking.id == id).first()


def get_all_bookings(db: Session):
    return db.query(DbBooking).all()


def delete_booking(db: Session, id: int):
    booking = db.query(DbBooking).filter(DbBooking.id == id).first()
    db.delete(booking)
    db.commit()
    return 'ok'



