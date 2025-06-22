from extensions import db
from sqlalchemy.orm import validates
from sqlalchemy_serializer import SerializerMixin


class Episode(db.Model, SerializerMixin):
    __tablename__ = 'episodes'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    number = db.Column(db.Integer)

    appearances = db.relationship(
        'Appearance', backref='episode', cascade='all, delete')

    serialize_rules = ('-appearances.episode',)


class Guest(db.Model, SerializerMixin):
    __tablename__ = 'guests'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    occupation = db.Column(db.String)

    appearances = db.relationship(
        'Appearance', backref='guest', cascade='all, delete')

    serialize_rules = ('-appearances.guest',)


class Appearance(db.Model, SerializerMixin):
    __tablename__ = 'appearances'
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer)

    guest_id = db.Column(db.Integer, db.ForeignKey('guests.id'))
    episode_id = db.Column(db.Integer, db.ForeignKey('episodes.id'))

    serialize_rules = ('-guest.appearances', '-episode.appearances')

    @validates('rating')
    def validate_rating(self, key, rating):
        if 1 <= rating <= 5:
            return rating
        raise ValueError("Rating must be between 1 and 5")
