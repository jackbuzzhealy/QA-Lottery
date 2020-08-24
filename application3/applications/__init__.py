from flask import Flask
import os

app = Flask(__name__)

from applications import routes
