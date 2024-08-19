from fastapi import APIRouter,Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserBase, UserDisplay
from db.database import get_db
from db import db_user #import create_user, get_user, update_user, delete_user, get_user_by_email



router = APIRouter(
    prefix = '/users',
    tags = ['users']
)

@router.post('/register', response_model = UserDisplay)
def register_user(request:UserBase,db: Session = Depends(get_db)):
    return db_user.create_user(db, request)

# @router.post('/login')
# def login(request: UserLogin, db: Session = Depends(get_db)):
#     user = get_user_by_email(db, request.email)
#     if not user or not Hash.verify(user.password, request.password):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
#     return {"access_token": access_token, "token_type": "bearer"}

@router.post('/login')#, response_model=UserDisplay)
def login_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.get_user_by_email(db, request.email)

@router.get('/{id}', response_model=UserDisplay)        #for get all users: response_model=List[UserDisplay]
def read_user(id: int, db: Session = Depends(get_db)):
    user = db_user.get_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put('/{id}', response_model=UserDisplay)
def update_user(id: int, request: UserBase, db: Session = Depends(get_db)):
    user = db_user.update_user(db, id, request)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete('/{id}', response_model=dict)
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db_user.delete_user(db, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
 