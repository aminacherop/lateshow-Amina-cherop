from app import app
from extensions import db
from models import Guest, Episode, Appearance
from faker import Faker
import random

fake = Faker()

with app.app_context():
    print("Dropping all tables...")
    db.drop_all()

    print("Creating tables...")
    db.create_all()

    print("Seeding database...")

    guests = []
    for _ in range(10):
        guest = Guest(
            name=fake.name(),
            occupation=fake.job()
        )
        db.session.add(guest)
        guests.append(guest)

    
    episodes = []
    for i in range(1, 6):
        episode = Episode(
            date=fake.date_between(start_date='-10y', end_date='today').strftime("%-m/%-d/%y"),
            number=i
        )
        db.session.add(episode)
        episodes.append(episode)

    db.session.commit()

    
    for _ in range(15):
        appearance = Appearance(
            rating=random.randint(1, 5),
            guest=random.choice(guests),
            episode=random.choice(episodes)
        )
        db.session.add(appearance)

    db.session.commit()
    print("Seeding complete.")
