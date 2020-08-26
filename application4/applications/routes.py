from applications import app
from flask import Response, request
from random import randint

@app.route('/postMyLighteningBall', methods=['POST'])
def postMyLighteningBall():
    post = request.data.decode('utf-8')
    myLighteningBall = int(post)

    winningLighteningBall = random.randint(1,14)

    match = bool 
    if myLighteningBall == winningLighteningBall:
        match = True
    else:
        match = False

    return Response(winningLighteningBall, mimetype='text/plain')

@app.route('/postMyLotteryNumbers', methods=['POST'])
def postMyLotteryNumbers():
    post = request.data.decode('utf-8')
    stringNumbers = list(post.split(" "))
    myLotteryNumbers = [int(i) for i in listRes] 

    count = 0
    winningNumbers = []
    while count != 6:
        ball = randint(1,50)
        if ball not in winningNumbers:
            winningNumbers.append(ball)
            count2 += 1
    list_string = map(str, winningNumbers)
    winningLotteryNumbers = " ".join(list_string)

    matches = 0
    for ball in myLotteryNumbers:
        if ball in winningNumbers:
            matches = matches + 1    
    return Response(winningLotteryNumbers, mimetype='text/plain')
