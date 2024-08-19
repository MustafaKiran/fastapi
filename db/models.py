from db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    bookings = relationship('DbBooking', back_populates='user')


class DbHotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    # star_rating = Column(Float)
    # phone_number = Column(String)
    # address = Column(String)
    # city = Column(String)
    # state = Column(String)
    # country = Column(String)
    # zip_code = Column(String)
    # latitude = Column(Float)
    # longitude = Column(Float)
    # number_of_rooms = Column(Integer)
    # room_types = Column(String)
    # price_per_night = Column(Float)
    bookings = relationship('DbBooking', back_populates='hotel')


class DbBooking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    hotel_id = Column(Integer, ForeignKey('hotels.id'))
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)

    user = relationship('DbUser', back_populates='bookings')
    hotel = relationship('DbHotel', back_populates='bookings')
