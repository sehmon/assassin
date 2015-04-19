from flask import render_template, redirect
from app import app, db, models
from models import Player

import twilio.twiml
from twilio.rest import TwilioRestClient

account_sid = "AC6202a281694e94d9df7485b5d21b5dcd"
auth_token  = "8b213cfb31f8b3e4a355fb913ebfde69"

client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello():

    players = models.Player.query.all()


    from_number = request.values.get('From', None)
    text = request.values.get('Body', None)
    print(text)

    # if from_number not in callers:


    return render_template("players.html", players=players)
