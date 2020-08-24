from applications import app
from flask import Response, request
from random import randint

@app.route('/postMyLighteningBall', methods=['POST'])
def postMyLighteningBall():
    myLighteningBall = request.data.decode('utf-8')
    winningLighteningBall = random.randint(1,14)

    match = bool 
    if myLighteningBall == winningLighteningBall:
        match = True
    else:
        match = False

    return Response(winningLighteningBall, mimetype='text/plain')

@app.route('/postMyLotteryNumbers', methods=['POST'])
def postMyLotteryNumbers():
    myLotteryNumbers = request.data.decode('utf-8')
    count = 1
    numbers = []
    while count != 6:
        numbers.append(random.randint(1,50)
        count = count + 1
    
    matches = int
    for ball in myLotteryNumbers:
        if ball in numbers:
            match = match + 1

    winningLotteryNumbers = " ".join(numbers)
    
    return Response(winningLotteryNumbers, mimetype='text/plain')
