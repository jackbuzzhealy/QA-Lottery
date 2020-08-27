from applications import app, db 
from applications.models import Prizes
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, jsonify
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generateLotteryNumbers', methods=['GET', 'POST'])
def generateLotteryNumbers():
    myLotteryNumbers = requests.get('http://app2:5001/getMyLotteryNumbers')
    response = requests.post('http://app4:5003/postMyLotteryNumbers', data=myLotteryNumbers.text)
    
    #get json TODO
    winnings = response.json()
    winningLotteryNumbers = winnings["winningBalls"]
    matches = winnings["matches"]

    #database prize
    qry = Prizes.query.filter_by(no_of_balls=matches).first()
    prize = 0
    if qry is None:
        prize = 0
    else:
        if matches == 1:
            prize = 0
        else:
            prize = qry.prize_value

    return render_template('lottery-result.html',myLotteryNumbers=myLotteryNumbers.text, winningLotteryNumbers=winningLotteryNumbers, prize=prize)

@app.route('/generateLighteningBall', methods=['GET', 'POST'])
def generateLighteningBall():
    myLighteningBall = requests.get('http://app3:5002/getMyLighteningBall')
    response = requests.post('http://app4:5003/postMyLighteningBall', data=myLighteningBall.text)

    #get boolean expression
    #database prize

    return render_template('lightening-ball-result.html', myLighteningBall=myLighteningBall.text, winningLighteningBall=winningLighteningBall.text)
