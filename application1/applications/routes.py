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
    
    winnings = response.json()
    winningLotteryNumbers = winnings["winningBalls"]
    matches = winnings["matches"]

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
    app.logger.info(myLighteningBall.text)
    response = requests.post('http://app4:5003/postMyLighteningBall', data=myLighteningBall.text)
    
    winnings = response.json()
    winningLighteningBall = winnings["winningBall"]
    matches = winnings["match"]

    prize = 0
    if matches == True:
        qry = Prizes.query.filter_by(lightening_ball="yes").first()
        prize = qry.prize_value

    return render_template('lightening-ball-result.html', myLighteningBall=myLighteningBall.text, prize=prize, winningLighteningBall=winningLighteningBall)
