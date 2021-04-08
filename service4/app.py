from flask import Flask
import random
import string

app = Flask(__name__)

@app.route('/getprize/<account>', methods=['POST'])
def getprize(account):
    prize = 0
    prizestring = account[0:5]
    prizeint = int(account[5:10])

    if prizeint % 10 == 0:
        prize += 1
    if prizeint % 3 == 0:
        prize += 2
    if prizeint % 7 == 0:
        prize += 3
    for i in prizestring:
        if i == 'f':
            prize += 1
        if i == 'q':
            prize += 1
        for d in prizestring:
            if i == d:
                prize += 1

    prize = prize*15

    return str(prize)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004,debug=True)
