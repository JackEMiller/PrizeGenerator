from flask import Flask
import random
import string

app = Flask(__name__)

@app.route('/createletters', methods=['GET'])
def createletters():
    letters = string.ascii_lowercase
    rndstring = ''.join(random.choice(letters) for i in range(5))
    return rndstring


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5002,debug=True)