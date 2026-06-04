from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
from enum import Enum


class HolesPlayedEnum(str, Enum):

    FRONT = "Front 9"
    BACK  = "Back 9"
    FULL =  "Full 18"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    handicap = Column(Float)
    email = Column(String, unique=True, index=True)
    home_location = Column(String, nullable=True)
    budget_per_round = Column(Float, nullable=True)
    travel_radius_miles = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship: A user can have many rounds
    rounds = relationship("Round", back_populates="user")

class Course(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(String)
    par = Column(Integer)
    rating = Column(Float)  # USGA course rating
    slope = Column(Float)   # USGA slope rating
    length = Column(Integer)  # Yards
    price = Column(Float)   # Green fee
    
    # Relationship: A course can have many rounds
    rounds = relationship("Round", back_populates="course")

class Round(Base):
    __tablename__ = "rounds"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    score = Column(Integer)
    holes_played = Column(String)
    tees = Column(String)
    date = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships: A round belongs to a user and a course
    user = relationship("User", back_populates="rounds")
    course = relationship("Course", back_populates="rounds")