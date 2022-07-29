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
    return render_template("pages/home.html")