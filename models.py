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
    snit = db.relationship("Snit", backref = "artist", lazy = True)

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
    snit = db.relationship("Snit", backref = "band", lazy = True)
        
    def __repr__(self):
        return f"<Band {self.name} {self.city}>"

class Snit(db.Model):
    __tablename__ = "snit"

    id = db.Column(db.Integer, primary_key = True)
    #snit_file = db.Column()
    snitted_by = db.Column(db.String, db.ForeignKey("artist.name"), nullable = True)
    snit_description = db.Column(db.String)
    #snit_date_time = db.Column(db.DateTime)

    def __repr__(self):
        return f"<Snit{self.snit_file} {self.snit_description} {self.snitted_by} {self.snit_date_time}"
    
