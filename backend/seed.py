from database import SessionLocal
from models import User, Course, Round

db = SessionLocal()

# Clear old data
db.query(Round).delete()
db.query(User).delete()
db.query(Course).delete()

# Add courses
courses = [
    Course(name="Cypress Creek", location="Austin, TX", par=72, rating=73.5, slope=135, length=6800, price=79),
    Course(name="Barton Creek", location="Austin, TX", par=72, rating=75.2, slope=142, length=7100, price=149),
    Course(name="Grey Rock", location="Kyle, TX", par=72, rating=71.8, slope=128, length=6500, price=49),
    Course(name="Jimmy Clay", location="Austin, TX", par=72, rating=72.1, slope=132, length=6700, price=59),
    Course(name="Walnut Creek", location="Austin, TX", par=71, rating=74.0, slope=140, length=6900, price=89),
    Course(name="Mount Bonnell", location="Austin, TX", par=72, rating=73.8, slope=138, length=6950, price=99),
    Course(name="Roy Kizer", location="Austin, TX", par=71, rating=70.5, slope=125, length=6300, price=45),
    Course(name="Onion Creek", location="Austin, TX", par=72, rating=76.0, slope=145, length=7200, price=129),
]

for course in courses:
    db.add(course)
db.commit()

# Add users
users = [
    User(name="John Doe", handicap=12, email="john@example.com"),
    User(name="Sarah Smith", handicap=8, email="sarah@example.com"),
    User(name="Mike Johnson", handicap=18, email="mike@example.com"),
]

for user in users:
    db.add(user)
db.commit()

# Add rounds for John Doe
john = db.query(User).filter(User.name == "John Doe").first()
john_rounds = [
    Round(user_id=john.id, course_id=1, score=85, tees="Blue", holes_played="Full"),
    Round(user_id=john.id, course_id=3, score=82, tees="White", holes_played="Full"),
    Round(user_id=john.id, course_id=4, score=88, tees="Blue", holes_played="Full"),
    Round(user_id=john.id, course_id=7, score=79, tees="White", holes_played="Full"),
]

# Add rounds for Sarah Smith
sarah = db.query(User).filter(User.name == "Sarah Smith").first()
sarah_rounds = [
    Round(user_id=sarah.id, course_id=1, score=78, tees="White", holes_played="Full"),
    Round(user_id=sarah.id, course_id=2, score=81, tees="Blue", holes_played="Full"),
    Round(user_id=sarah.id, course_id=5, score=75, tees="White", holes_played="Full"),
]

# Add rounds for Mike Johnson
mike = db.query(User).filter(User.name == "Mike Johnson").first()
mike_rounds = [
    Round(user_id=mike.id, course_id=3, score=92, tees="Red", holes_played="Full"),
    Round(user_id=mike.id, course_id=4, score=95, tees="Red", holes_played="Full"),
    Round(user_id=mike.id, course_id=7, score=88, tees="White", holes_played="Full"),
]

all_rounds = john_rounds + sarah_rounds + mike_rounds
for round_data in all_rounds:
    db.add(round_data)

db.commit()
print("Sample data added!")
print(f"   - {len(users)} users")
print(f"   - {len(courses)} courses")
print(f"   - {len(all_rounds)} rounds")