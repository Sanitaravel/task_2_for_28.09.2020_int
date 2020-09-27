from flask import *

app = Flask(__name__)


counter = 0

@app.route('/')
def print():
    global counter
    if request.method == 'GET':
        counter+=1
        return f'Привет, {counter}-ый посетитель!'