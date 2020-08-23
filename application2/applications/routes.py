from applications import app
from flask import Response, request
from random import randint 

@app.route('/getAnimal', methods=['GET'])
def getLighteningBall():
    
    return Response(animal, mimetype="text/plain")

@app.route('/getNoise', methods=['POST'])
def getNoise():
    animal = request.data.decode('utf-8')
    if animal == "Dog":
        noise = "Woof!"
    elif animal == "Cat":
        noise = "Meow!"
    elif animal == "Mouse":
        noise = "Squeak!"
    elif animal == "Horse":
        noise = "Neigh!"
    elif animal == "Cow":
        noise = "Moo!"
    elif animal == "Sheep":
        noise = "Baa!"
    else:
        noise = "Unknown!"
    
    return Response(noise, mimetype='text/plain')
