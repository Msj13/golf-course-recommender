from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from analytics import get_score_trend
from database import engine, get_db, Base
from models import User, Course, Round
from enum import Enum

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



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

class RecommendationRequest(BaseModel):
    user_id: int
    location: str
    max_price: float = 100.0
    difficulty: str = "any"


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


@app.get("/recommendations/{user_id}")
def recommend_courses(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    
    # Get user's past rounds
    user_rounds = db.query(Round).filter(Round.user_id == user_id).all()
    user_avg_score = sum([r.score for r in user_rounds]) / len(user_rounds) if user_rounds else 0
    
    # Get all courses
    all_courses = db.query(Course).all()
    
    # Simple scoring: courses matching user's difficulty + cheaper options
    scored = []
    for course in all_courses:
        # Skip courses user already played
        if any(r.course_id == course.id for r in user_rounds):
            continue
        
        score = 50
        # Favor courses close to user's average score
        if abs(course.rating - user.handicap) < 3:
            score += 25
        # Favor cheaper courses
        if course.price < 80:
            score += 15
        
        scored.append({"course": course, "score": score})
    
    # Sort by score
    scored.sort(key=lambda x: x["score"], reverse=True)
    
    # Return top 5
    return {
        "user": user.name,
        "recommendations": [
            {
                "name": s["course"].name,
                "location": s["course"].location,
                "price": s["course"].price,
                "rating": s["course"].rating,
                "match_score": s["score"]
            }
            for s in scored[:5]
        ]
    }

@app.get("/users/")
def list_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "name": u.name, "handicap": u.handicap} for u in users]

@app.get("/courses/")
def list_courses(db: Session = Depends(get_db)):
    courses = db.query(Course).all()
    return [{"id": c.id, "name": c.name, "location": c.location, "price": c.price, "rating": c.rating} for c in courses]


@app.get("/users/{user_id}/stats")
def user_stats(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "User not found"}
    
    rounds = db.query(Round).filter(Round.user_id == user_id).all()
    
    if not rounds:
        return {"name": user.name, "rounds_played": 0, "avg_score": 0}
    
    avg_score = sum([r.score for r in rounds]) / len(rounds)
    best_score = min([r.score for r in rounds])
    
    return {
        "name": user.name,
        "handicap": user.handicap,
        "rounds_played": len(rounds),
        "avg_score": round(avg_score, 1),
        "best_score": best_score
    }

@app.get("/rounds/user/{user_id}")
def get_user_rounds(user_id: int, db: Session = Depends(get_db)):
    rounds = db.query(Round).filter(Round.id == user_id).all()

    if not rounds:
        return []
    

    return [
        {
            "id": r.id,
            "course_id": r.course_id,
            "score": r.score,
            "tees": r.tees,
            "holes_played": r.holes_played,
            "date": r.date,
            "course_name": db.query(Course).filter(Course.id == r.course_id).first().name
        }

        for r in rounds
    ]

@app.get("/analytics/score-trend/{user_id}")
def get_score_trend_endpoint(user_id: int, db: Session = Depends(get_db)):
    user_rounds = db.query(Round).filter(Round.user_id == user_id).all()

    return get_score_trend(user_rounds)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


