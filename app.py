import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, Response, flash, redirect, url_for
import json
import dateutil.parser
import babel
from flask_moment import Moment
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
from flask_migrate import Migrate
from models import *

app = Flask(__name__)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


@app.route("/")
def index():
    selection = Artist.query.all()
    return render_template("pages/home.html")

@app.route("/search", methods=["POST"])
def search():
    search_term = request.form.get("search_term")
    artist_response = Artist.query.filter((Artist.name.ilike("%" + search_term + "%" )))
    band_response = Band.query.filter((Band.name.ilike("%" + search_term + "%")))

    return render_template("pages/search_artist", results = artist_response, response = band_response)

@app.route("/artists/<int:artist_id>")
def show_artist(artist_id):
    data = Artist.query.get(artist_id)
    snits = Snit.query.join(Aritst, Snit.)
    