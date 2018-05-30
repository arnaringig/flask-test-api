#!flask/bin/python
from flask import Flask, jsonify

import prufa
import time


app = Flask(__name__)


@app.route('/cola', methods=['GET'])
def reikna():
    tala = 100
    return str(tala)

@app.route('/post/<int:tala>')
def fall(tala):
    ta = tala*200
    return 'talan er %d' % ta


if __name__ == '__main__':
    app.run(debug=True)