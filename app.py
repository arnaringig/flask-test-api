#!flask/bin/python
from flask import Flask, jsonify
from qs import quicksortLomuto, swap, partition


import time

def fall(tala):
    ta = tala*200
    return str(ta)

app = Flask(__name__)



@app.route('/cola', methods=['GET'])
def reikna():
    tala = 100
    return str(tala)

@app.route('/post/<int:tala>')
def bro(tala):
    return fall(2)

@app.route('/prufa/')
def brom():
    return quicksortLomuto([3,6,5,1,7],0,4)


if __name__ == '__main__':
    app.run(debug=True)