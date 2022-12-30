import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date, datetime


# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/works", methods=["GET", "POST"])
def works():
    return render_template("works.html")

@app.route("/about", methods=["GET", "POST"])
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    return render_template("contact.html")