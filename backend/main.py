from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from database import engine, get_db, Base
from models import User, Course, Round
from enum import Enum

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    handicap: float
    email: str


class CourseCreate(BaseModel):
    name: str
    location: str
    par: int
    rating: float
    slope: float
    length: int
    price: float


class HolesPlayedEnum(str, Enum):
    FRONT = "Front"
    BACK = "Back"
    FULL = "Full"

class RoundCreate(BaseModel):
    user_id: int
    course_id: int
    score: int
    tees: str
    holes_played: HolesPlayedEnum


@app.post("/courses/")
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(name=course.name, location=course.location, par=course.par, rating=course.rating, slope=course.slope, length=course.length, price=course.price)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return db_course

@app.get("/courses/{course_id}")
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        return {"Error:": "Course not found"}

    return course

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name = user.name, handicap=user.handicap, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"Error": "User not found"}
    return user


@app.post("/round/")
def create_round(round: RoundCreate, db: Session = Depends(get_db)):

    db_round = Round(
    user_id=round.user_id, 
    course_id=round.course_id, 
    score=round.score, 
    holes_played=round.holes_played, 
    tees=round.tees  # Changed from tees_played
    )
    db.add(db_round)
    db.commit()
    db.refresh(db_round)
    
    return db_round

@app.get("/round/{round_id}")
def get_round(round_id: int, db: Session = Depends(get_db)):
    round = db.query(Round).filter(Round.id == round_id).first()

    if not round:
        return {"error": "round not found"}

    return round


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


