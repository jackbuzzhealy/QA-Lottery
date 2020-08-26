from applications import app, db 
from applications.models import Prizes
from flask import render_template
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generateLotteryNumbers', methods=['GET', 'POST'])
def generateLighteningBall():
    myLighteningBall = requests.get('http://app2:5001/getMyLotteryNumbers')
    winningLighteningBall = requests.post('http://app4:5003/postMyLotteryNumbers', data=myLighteningBall.text)
    return render_template('lightening-ball-result.html', myLighteningBall=myLighteningBall.text, winningLighteningBall=winningLighteningBall.text)

@app.route('/generateLighteningBall', methods=['GET', 'POST'])
def generateLotteryNumbers():
    myLotteryNumbers = requests.get('http://app3:5002/getMyLighteningBall')
    winningLotteryNumbers = requests.post('http://app4:5003/postMyLighteningBall', data=myLotteryNumbers.text)
    return render_template('lottery-result.html', myLotteryNumbers=myLotteryNumbers.text, winningLotteryNumbers=winningLotteryNumbers.text)
