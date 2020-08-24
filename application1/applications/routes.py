from applications import app, db 
from applications.models import Prizes
from flask import render_template
import requests

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/generateLotteryNumbers', methods=['GET', 'POST'])
def generateLighteningBall():
    myLigteningBall = requests.get('http://app2:5001/getMyLotteryNumbers')
    winningLighteningBall = requests.post('http://app2:5003/postMyLotteryNumbers', data=myLigteningBall.number)
    return render_template('lightening-ball-result.html', myLigteningBall=myLigteningBall.number, winningLighteningBall=winningLighteningBall.text)

@app.route('/generateLighteningBall', methods=['GET', 'POST'])
def generateLotteryNumbers():
    myLotteryNumber = requests.get('http://app2:5002/getMyLighteningBall')
    winningLotteryNumbers = requests.post('http://app2:5003/postMyLighteningBall', data=myLotteryNumber.number)
    return render_template('lottery-result.html', myLotteryNumber=myLotteryNumber.number, winningLotteryNumbers=winningLotteryNumbers.text)