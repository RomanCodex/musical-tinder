import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Artist, Venue, Band

class MusicalTinderTestCase(unittest.TestCase):
    """This class represents the test cases for the app"""

    def setUp(self):
        """Define test variables and init app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "tinder_test"
        self.database_path = "postgresql://{}@{}/{}". format("postgres:abc","localhost:5432", self.database_name)
        setup_db(self.app, self.database_path)

        self.new_artist = {"name": "Renegade", "city": "Ibadan", "state": "Oyo", "current_address": "No 9b, Anthony Estate, Aba-Eleshin, Apata", "phone_number": "08144632746", "image_link": "https://images.com/renegade", "genres": "Blues", "website_link": "https://www.renegade.com", "current_band": "None", "seeking_band": False, "seeking_description": "None"}

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)

            self.db.create_all()
        
    def tearDown(self):
        """After every test """
        pass
    
    def test_get_artist(self):
        res = self.client().get("/artists")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["artists"])
        self.assertTrue(len(data["artists"]))

        