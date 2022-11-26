from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def hello():
    return  '<h1>Hello my friend!</h1> \
            <p>Your lucky number: {}</p>'.format(random.randint(1,99))