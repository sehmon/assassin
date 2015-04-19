from flask import render_template, redirect, request
from app import app, db, models
from models import Player

import twilio.twiml
from twilio.rest import TwilioRestClient

account_sid = "AC6202a281694e94d9df7485b5d21b5dcd"
auth_token  = "8b213cfb31f8b3e4a355fb913ebfde69"


@app.route("/", methods=['GET', 'POST'])
def hello():

    players = models.Player.query.all()

    if request.method == 'POST':
        from_number = request.values.get('From', None)
        text = request.values.get('Body', None)
        print(text)
        client = TwilioRestClient(account_sid, auth_token)


    return render_template("players.html", players=players)



@app.route("/players", methods=['GET', 'POST'])
def players():
    
    body = request.values.get('Body', None)
    from_number = request.values.get('From', None)

    resp = twilio.twiml.Response()
    resp.message(body+" "+from_number)
    return str(resp)
