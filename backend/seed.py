import random
from faker import Faker
from database import SessionLocal, Base, engine
from models import User, Course, Round

Base.metadata.create_all(bind=engine)

fake = Faker()
db = SessionLocal()

# Clear existing data
db.query(Round).delete()
db.query(User).delete()
db.query(Course).delete()
db.commit()

# Texas courses
texas_courses = [
    ("Barton Creek Resort", "Austin, TX", 72, 75.2, 142, 7100, 149),
    ("Cypress Creek", "Houston, TX", 72, 73.5, 135, 6800, 79),
    ("Grey Rock Golf Club", "Austin, TX", 72, 71.8, 128, 6500, 49),
    ("Jimmy Clay Golf Course", "Austin, TX", 72, 72.1, 132, 6700, 59),
    ("Roy Kizer Golf Course", "Austin, TX", 71, 70.5, 125, 6300, 45),
    ("Walnut Creek Golf Course", "Austin, TX", 71, 74.0, 140, 6900, 89),
    ("Onion Creek Club", "Austin, TX", 72, 76.0, 145, 7200, 129),
    ("Mount Bonnell Golf", "Austin, TX", 72, 73.8, 138, 6950, 99),
    ("TPC San Antonio", "San Antonio, TX", 72, 76.5, 148, 7400, 200),
    ("Brackenridge Park", "San Antonio, TX", 72, 70.2, 122, 6200, 39),
    ("Cowboys Golf Club", "Grapevine, TX", 72, 74.8, 138, 7000, 129),
    ("Whispering Pines", "Trinity, TX", 72, 75.5, 143, 7100, 159),
    ("Colonial Country Club", "Fort Worth, TX", 70, 74.2, 139, 7080, 175),
    ("Omni Barton Creek", "Austin, TX", 72, 74.5, 140, 6956, 185),
    ("Lost Pines Golf Club", "Bastrop, TX", 72, 73.2, 133, 6800, 95),
    ("Falconhead Golf Club", "Austin, TX", 72, 72.8, 130, 6750, 75),
    ("Forest Creek Golf Club", "Round Rock, TX", 72, 73.0, 131, 6845, 65),
    ("Avery Ranch Golf Club", "Austin, TX", 72, 72.5, 129, 6700, 69),
    ("Berry Creek Country Club", "Georgetown, TX", 72, 73.8, 136, 6900, 89),
    ("Wild Rock Golf Club", "Georgetown, TX", 72, 74.1, 137, 6950, 99),
    ("Plum Creek Golf Course", "Kyle, TX", 72, 71.5, 126, 6550, 55),
    ("Dry Creek Ranch Golf", "Hutto, TX", 72, 72.3, 130, 6700, 65),
    ("Teravista Golf Club", "Round Rock, TX", 72, 73.5, 134, 6850, 79),
    ("Legacy Hills Golf Club", "Georgetown, TX", 72, 74.0, 138, 6950, 95),
    ("San Saba River Valley", "San Saba, TX", 72, 70.8, 124, 6400, 45),
]

# Florida courses
florida_courses = [
    ("TPC Sawgrass", "Ponte Vedra Beach, FL", 72, 76.8, 155, 7215, 250),
    ("Bay Hill Club", "Orlando, FL", 72, 75.5, 148, 7239, 200),
    ("Doral Golf Resort", "Miami, FL", 72, 75.2, 145, 7125, 175),
    ("PGA National", "Palm Beach Gardens, FL", 72, 76.0, 150, 7048, 225),
    ("Innisbrook Resort", "Palm Harbor, FL", 71, 75.8, 146, 7340, 195),
    ("Grand Cypress Golf", "Orlando, FL", 72, 74.5, 140, 6906, 165),
    ("Tiburón Golf Club", "Naples, FL", 72, 75.0, 144, 7288, 185),
    ("Streamsong Resort", "Bowling Green, FL", 72, 74.8, 141, 7149, 195),
    ("Seminole Golf Club", "Juno Beach, FL", 72, 75.3, 143, 6900, 210),
    ("World Woods Golf Club", "Brooksville, FL", 72, 73.8, 136, 6985, 89),
    ("Cabot Citrus Farms", "Brooksville, FL", 72, 74.2, 138, 7050, 175),
    ("Orange County National", "Winter Garden, FL", 72, 73.5, 134, 7200, 79),
    ("Reunion Resort", "Kissimmee, FL", 72, 74.0, 137, 7100, 145),
    ("Valhalla Bay Golf", "Tampa, FL", 72, 73.2, 132, 6900, 95),
    ("Shark's Tooth Golf", "Port St. Lucie, FL", 72, 73.8, 135, 7050, 85),
    ("Myrtlewood Golf Club", "Myrtle Beach, FL", 72, 72.5, 129, 6700, 69),
    ("Eagle Dunes Golf", "Sorrento, FL", 72, 72.8, 131, 6800, 75),
    ("Hammock Dunes Club", "Palm Coast, FL", 72, 74.5, 140, 7015, 155),
    ("Interlachen Country Club", "Winter Park, FL", 72, 74.8, 142, 6956, 165),
    ("MetroWest Golf Club", "Orlando, FL", 72, 73.0, 130, 6823, 65),
    ("Hunters Creek Golf", "Orlando, FL", 72, 72.3, 128, 6738, 55),
    ("Falcon's Fire Golf", "Kissimmee, FL", 72, 73.5, 133, 6901, 79),
    ("Celebration Golf Club", "Celebration, FL", 72, 73.8, 135, 6783, 85),
    ("Tranquilo Golf Club", "Four Corners, FL", 72, 72.8, 130, 6854, 75),
    ("Buffalo Creek Golf", "Palmetto, FL", 72, 72.5, 128, 6717, 65),
]

# Arizona courses
arizona_courses = [
    ("TPC Scottsdale", "Scottsdale, AZ", 71, 73.5, 135, 7216, 225),
    ("Troon North Golf Club", "Scottsdale, AZ", 72, 74.8, 144, 7008, 195),
    ("We-Ko-Pa Golf Club", "Scottsdale, AZ", 72, 75.2, 147, 7225, 185),
    ("Grayhawk Golf Club", "Scottsdale, AZ", 72, 74.5, 141, 6973, 175),
    ("Desert Mountain Club", "Scottsdale, AZ", 72, 75.0, 145, 7105, 200),
    ("Whisper Rock Golf Club", "Scottsdale, AZ", 72, 75.5, 148, 7154, 215),
    ("Boulders Club", "Carefree, AZ", 71, 73.8, 137, 6811, 165),
    ("Arizona Biltmore", "Phoenix, AZ", 71, 72.5, 130, 6300, 145),
    ("Wigwam Golf Resort", "Litchfield Park, AZ", 72, 74.2, 139, 7030, 155),
    ("Talking Stick Golf", "Scottsdale, AZ", 71, 72.8, 131, 6833, 89),
    ("Camelback Golf Club", "Scottsdale, AZ", 72, 73.5, 134, 6924, 95),
    ("Papago Golf Course", "Phoenix, AZ", 71, 72.0, 127, 6708, 45),
    ("Encanto Golf Course", "Phoenix, AZ", 70, 69.5, 119, 6200, 35),
    ("Dobson Ranch Golf", "Mesa, AZ", 72, 72.3, 129, 6680, 55),
    ("Las Sendas Golf Club", "Mesa, AZ", 72, 73.8, 136, 6888, 79),
    ("Superstition Springs", "Mesa, AZ", 72, 73.2, 132, 6845, 69),
    ("Gold Canyon Golf", "Gold Canyon, AZ", 72, 74.0, 138, 6900, 99),
    ("Pointe Hilton Tapatio", "Phoenix, AZ", 72, 73.5, 134, 6865, 89),
    ("Raven Golf Club", "Phoenix, AZ", 72, 74.2, 139, 7078, 95),
    ("Stonecreek Golf Club", "Phoenix, AZ", 71, 72.8, 131, 6839, 75),
    ("Sunridge Canyon Golf", "Fountain Hills, AZ", 71, 73.5, 135, 6823, 85),
    ("Eagle Mountain Golf", "Fountain Hills, AZ", 71, 73.2, 132, 6755, 79),
    ("FireRock Country Club", "Fountain Hills, AZ", 72, 74.5, 141, 7005, 145),
    ("Rio Verde Country Club", "Rio Verde, AZ", 72, 73.0, 130, 6700, 65),
    ("Tonto Verde Golf Club", "Rio Verde, AZ", 72, 73.8, 136, 6850, 85),
]

# California courses
california_courses = [
    ("Pebble Beach Golf Links", "Pebble Beach, CA", 72, 75.5, 145, 6828, 575),
    ("Spyglass Hill", "Pebble Beach, CA", 72, 75.3, 148, 6960, 350),
    ("Torrey Pines South", "La Jolla, CA", 72, 76.1, 150, 7607, 225),
    ("Riviera Country Club", "Pacific Palisades, CA", 71, 75.2, 145, 7322, 300),
    ("Pelican Hill Golf", "Newport Beach, CA", 71, 74.5, 141, 6856, 265),
    ("Sherwood Country Club", "Thousand Oaks, CA", 72, 75.0, 144, 7025, 285),
    ("Tehama Golf Club", "Carmel, CA", 72, 74.8, 142, 6924, 275),
    ("Pasatiempo Golf Club", "Santa Cruz, CA", 71, 73.8, 138, 6483, 195),
    ("The Links at Spanish Bay", "Pebble Beach, CA", 72, 74.2, 139, 6960, 295),
    ("Monarch Beach Golf", "Dana Point, CA", 70, 72.5, 130, 6069, 145),
    ("Aviara Golf Club", "Carlsbad, CA", 72, 75.2, 147, 7007, 225),
    ("Crossroads Golf Club", "San Diego, CA", 72, 73.5, 134, 6800, 89),
    ("Rancho Bernardo Inn", "San Diego, CA", 72, 73.8, 136, 6936, 95),
    ("Maderas Golf Club", "Poway, CA", 72, 74.5, 141, 7099, 115),
    ("Barona Creek Golf Club", "Lakeside, CA", 72, 74.8, 142, 7088, 125),
    ("Steele Canyon Golf", "Jamul, CA", 72, 74.2, 138, 7017, 105),
    ("Sycuan Golf Resort", "El Cajon, CA", 72, 73.5, 134, 6924, 95),
    ("Coronado Golf Course", "Coronado, CA", 72, 72.8, 130, 6599, 75),
    ("Balboa Park Golf", "San Diego, CA", 72, 72.0, 126, 6400, 45),
    ("Torrey Pines North", "La Jolla, CA", 72, 74.2, 138, 7020, 145),
    ("La Costa Resort", "Carlsbad, CA", 72, 74.8, 142, 7021, 195),
    ("Omni La Costa", "Carlsbad, CA", 72, 74.5, 140, 6894, 175),
    ("Park Hyatt Aviara", "Carlsbad, CA", 72, 75.0, 144, 7007, 215),
    ("The Grand Golf Club", "San Diego, CA", 72, 74.2, 139, 7156, 165),
    ("Encinitas Ranch Golf", "Encinitas, CA", 72, 73.5, 134, 6587, 85),
]

# Combine all courses
all_courses = texas_courses + florida_courses + arizona_courses + california_courses

# Add courses to database
course_objects = []
for name, location, par, rating, slope, length, price in all_courses:
    course = Course(
        name=name,
        location=location,
        par=par,
        rating=rating,
        slope=slope,
        length=length,
        price=price
    )
    db.add(course)
    course_objects.append(course)

db.commit()
print(f"✅ Added {len(course_objects)} courses")

# Generate 100 users
tee_options = ["Red", "White", "Blue", "Black", "Gold"]
holes_options = ["Front", "Back", "Full"]

home_cities = [
    "Austin, TX", "Houston, TX", "San Antonio, TX", "Dallas, TX",
    "Orlando, FL", "Miami, FL", "Tampa, FL", "Jacksonville, FL",
    "Phoenix, AZ", "Scottsdale, AZ", "Tucson, AZ",
    "San Diego, CA", "Los Angeles, CA", "San Francisco, CA",
]

user_objects = []
for i in range(100):
    user = User(
        name=fake.name(),
        handicap=round(random.uniform(2, 28), 1),
        email=fake.unique.email(),
        home_location=random.choice(home_cities),
        budget_per_round=round(random.uniform(40, 200), 2),
        travel_radius_miles=random.choice([25, 50, 100, 250, 500]),
    )
    db.add(user)
    user_objects.append(user)

db.commit()
print(f"✅ Added {len(user_objects)} users")

# Generate rounds for each user
round_count = 0
for user in user_objects:
    num_rounds = random.randint(5, 25)
    
    for _ in range(num_rounds):
        # Pick a random course
        course = random.choice(course_objects)
        
        # Generate realistic score based on handicap
        base_score = course.par + user.handicap + random.uniform(-3, 8)
        score = round(base_score)
        
        db.add(Round(
            user_id=user.id,
            course_id=course.id,
            score=score,
            tees=random.choice(tee_options),
            holes_played=random.choice(holes_options)
        ))
        round_count += 1

db.commit()
print(f"✅ Added {round_count} rounds")
print(f"\n🏌️ Database seeded successfully!")
print(f"   - 100 courses across TX, FL, AZ, CA")
print(f"   - 100 users")
print(f"   - {round_count} rounds")