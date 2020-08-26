from applications import app
from flask import Response, request
from random import randint 

@app.route('/getMyLotteryNumbers', methods=['GET'])
def getMyLotteryNumbers():
    count = 0
    myNumbers = []
    while count != 6:
        ball = randint(1,50)
        if ball not in myNumbers:
            myNumbers.append(ball)
            count1 += 1
    list_string = map(str, myNumbers)
    myLotteryNumbers = " ".join(list_string)
    return Response(myLotteryNumbers, mimetype="text/plain")
