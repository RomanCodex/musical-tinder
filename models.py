import os
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "musical_tinder"
database_path = "postgresql://{}@{}/{}".format("postgres:abc", "localhost:5432", self.database_name)

db = SQLAlchemy()

"""
setup_db(app)
    binds the application and a SQLAlchemy service
"""

def setup_db(app, database_path = database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()

"""
Artist

"""

class Artist(db.Model):
    __tablename__ = "artist"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    current_address = db.Column(db.String)
    phone_number = db.Column(db.String)
    image_link = db.Column(db.String)
    genres = db.Column(db.String)
    website_link = db.Column(db.String)
    current_band = db.relationship("Band", backref = "artist", lazy = True)
    seeking_band = db.Column(db.Boolean(), default = False)
    seeking_description = db.Column(db.String)

    def __init__(self, name, city, state, current_address, phone_number, image_link, genres, website_link, seeking_band, current_band, seeking_description):
        self.name = name
        self.city = city
        self.state = state
        self.current_address = current_address
        self.phone_number = phone_number
        self.image_link = image_link
        self.genres = genres
        self.website_link = website_link
        self.current_band = current_band
        self.seeking_band = seeking_band
        self.seeking_description = seeking_description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Artist {self.name}>"

class Band(db.Model):
    __tablename__ = "band"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    city = db.Column(db.String)
    state = db.Column(db.String)
    current_hq = db.Column(db.String)
    phone_number = db.Column(db.String)
    image_link = db.Column(db.String)
    genres = db.Column(db.String)
    website_link = db.Column(db.String)
    member_1 = db.Column(db.String, db.ForeignKey("artist.name"), nullable = False)
    member_2 = db.Column(db.String, db.ForeignKey("artist.name"), nullable = True)
    member_3 = db.Column(db.String, db.ForeignKey("artist.name"), nullable = True)
    member_4 = db.Column(db.String, db.ForeignKey("artist.name"), nullable = True)
    seeking_member = db.Column(db.Boolean(), default = False)
    seeking_description = db.Column(db.String)

    def __init__(self, name, city, state, current_address, phone_number, image_link, genres, website_link, seeking_member, member_1, member_2, member_3, member_4, seeking_description):
        self.name = name
        self.city = city
        self.state = state
        self.current_address = current_address
        self.phone_number = phone_number
        self.image_link = image_link
        self.genres = genres
        self.website_link = website_link
        self.member_1 = member_1
        self.member_2 = member_2
        self.member_3 = member_3
        self.member_4 = member_4
        self.seeking_member = seeking_member
        self.seeking_description = seeking_description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
    def __repr__(self):
        return f"<Band {self.name} {self.city}>"