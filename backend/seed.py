from database import SessionLocal
from models import User, Course, Round

db = SessionLocal()

# Add sample courses
courses = [
    Course(name="Cypress Creek", location="Austin, TX", par=72, rating=73.5, slope=135, length=6800, price=79),
    Course(name="Barton Creek", location="Austin, TX", par=72, rating=75.2, slope=142, length=7100, price=149),
    Course(name="Grey Rock", location="Austin, TX", par=72, rating=71.8, slope=128, length=6500, price=49),
    Course(name="Jimmy Clay", location="Austin, TX", par=72, rating=72.1, slope=132, length=6700, price=59),
    Course(name="Walnut Creek", location="Austin, TX", par=71, rating=74.0, slope=140, length=6900, price=89),
]

for course in courses:
    db.add(course)

# Add sample user
user = User(name="John Doe", handicap=12, email="john@example.com")
db.add(user)
db.commit()

# Add sample rounds
user_id = user.id
for i, course in enumerate(courses[:3]):
    round_data = Round(user_id=user_id, course_id=course.id, score=85 - i*2, tees="Blue", holes_played="Full")
    db.add(round_data)

db.commit()
print("Sample data added!")