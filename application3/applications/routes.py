from applications import app
from flask import Response, request
from random import randint 

@app.route('/getMyLighteningBall', methods=['GET'])
def getMyLighteningBall():
    myLighteningBall = random.randint(1,14)
    return Response(myLighteningBall, mimetype="text/plain")
