from applications import app
from flask import Response, request
from random import randint 

@app.route('/getMyLighteningBall', methods=['GET'])
def getMyLighteningBall():
    myLighteningBall = random.randint(1,14)
    return Response(myLighteningBall, mimetype="number/plain")

@app.route('/postMyLighteningBall', methods=['POST'])
def postMyLighteningBall():
    myLighteningBall = request.data.decode('utf-8')
    winningLighteningBall = random.randint(1,14)
    return Response(winningLighteningBall, mimetype='number/plain')

@app.route('/getMyLotteryNumbers', methods=['GET'])
def getMyLotteryNumbers():
    count = 1
    myLotteryNumbers = []
    while count != 6:
        myLotteryNumbers.append(random.randint(1,50)
        count = count + 1

    return Response(LotteryNumbers, mimetype="number/plain")

@app.route('/postMyLotteryNumbers', methods=['POST'])
def postMyLotteryNumbers():
    myLotteryNumbers = request.data.decode('utf-8')
    count = 1
    winningLotteryNumbers = []
    while count != 6:
        winningLotteryNumbers.append(random.randint(1,50)
        count = count + 1

    return Response(winningLotteryNumbers, mimetype='number/plain')
