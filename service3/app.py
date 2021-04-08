from flask import Flask
import random
import string

app = Flask(__name__)

@app.route('/createnumber', methods=['GET'])
def createnumber():
    rndstring = str(random.randint(10000,99999))
    return rndstring


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5003,debug=True)