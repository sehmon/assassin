from flask import render_template, redirect
from app import app

@app.route("/")
def hello():
    return "Hello World!"
