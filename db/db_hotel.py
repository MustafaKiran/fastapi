from sqlalchemy.orm.session import Session
from db.models import DbHotel
from schemas import HotelBase

def create_hotel(db: Session, request: HotelBase):
  new_hotel = DbHotel(
    name = request.name,
    description = request.description,
    # star_rating = request.star_rating,
    # phone_number = request.phone_number,
    # address = request.address,
    # city = request.city,
    # state = request.state,
    # country = request.country,
    # zip_code = request.zip_code,
    # latitude = request.latitude,
    # longitude = request.longitude,
    # number_of_rooms  = request.number_of_rooms,
    # room_types = request.room_types,
    # price_per_night = request.price_per_night,
    
  )
  db.add(new_hotel)
  db.commit()
  db.refresh(new_hotel)
  return new_hotel

def get_hotel(db: Session, id: int):
  hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
  # Handle errors
  return hotel

def get_all_hotel(db: Session):
  return db.query(DbHotel).all()

def update_hotel(db: Session, id: int, request: HotelBase):
  hotel = db.query(DbHotel).filter(DbHotel.id == id)
  hotel.update({
    DbHotel.name: request.name,
    DbHotel.description: request.description,
    # DbHotel.phone_number: request.phone_number,
    # DbHotel.number_of_rooms: request.number_of_rooms,
    # DbHotel.room_types: request.room_types,
    # DbHotel.price_per_night: request.price_per_night,
    
  })
  db.commit()
  return 'ok'



def delete_hotel(db: Session, id: int):
  hotel = db.query(DbHotel).filter(DbHotel.id == id).first()
  db.delete(hotel)
  db.commit()
  return 'ok'