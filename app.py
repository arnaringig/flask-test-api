#!flask/bin/python
from flask import Flask, jsonify
from qs import quicksortLomuto, swap, partition


import time

def fall(tala):
    ta = tala*200
    return str(ta)

arri = [8,10,1,2,9,7,4,5,8,6,4,5,6,5,2,3,5,76,4,3,2]

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
    return quicksortLomuto(arri,0,len(arri)-1)


if __name__ == '__main__':
    app.run(debug=True)