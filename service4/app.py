from flask import Flask
import random
import string

app = Flask(__name__)

@app.route('/getprize/<string>', methods=['POST'])
def getprize(string):
    prize = 0
    prizestring = string[0:5]
    prizeint = int(string[5:10])

    if prizeint % 10 == 0:
        prize += 1
    if prizeint % 3 == 0:
        prize += 2
    if prizeint % 7 == 0:
        prize += 3
    for i in prizestring:
        for d in prizestring:
            if i == d:
                prize += 1

    prize = prize*15

    return str(prize)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)
