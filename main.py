from fastapi import FastAPI
from db.database import engine, Base
from router import users, hotels, bookings
from auth import authentication

app = FastAPI()


Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(hotels.router)
app.include_router(bookings.router)