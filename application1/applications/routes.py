from applications import app, db 
from applications.models import Prizes
from flask import render_template
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generateLighteningBall', methods=['GET', 'POST'])
def generateLighteningBall():
    myLigteningBall = requests.get('http://app2:5001/getMyLighteningBall')
    winningLighteningBall = requests.post('http://app2:5001/postMyLighteningBall', data=myLigteningBall.number)
    return render_template('lightening-ball-result.html', myLigteningBall=myLigteningBall.number, winningLighteningBall=winningLighteningBall.number)

@app.route('/generateLotteryNumbers', methods=['GET', 'POST'])
def generateLotteryNumbers():
    myLotteryNumber = requests.get('http://app2:5001/getMyLighteningBall')
    winningLotteryNumbers = requests.post('http://app2:5001/postMyLighteningBall', data=myLotteryNumber.number)
    return render_template('lottery-result.html', myLotteryNumber=myLotteryNumber.number, winningLotteryNumbers=winningLotteryNumbers.number)
