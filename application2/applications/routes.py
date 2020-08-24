from applications import app
from flask import Response, request
from random import randint 

@app.route('/getMyLotteryNumbers', methods=['GET'])
def getMyLotteryNumbers():
    count = 1
    numbers = []
    while count != 6:
        numbers.append(random.randint(1,50)
        count = count + 1

    myLotteryNumbers = " ".join(numbers)

    return Response(myLotteryNumbers, mimetype="text/plain")
