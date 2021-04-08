from flask import Flask, request, render_template
import requests
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        responsea = requests.get('http://service2:5002/createletters').text
        responseb = requests.get('http://service3:5003/createnumber').text
        responsec = requests.post('http://service4:5004/getprize/'+ responsea + responseb).text
        return render_template('index.html', prizestring = responsea, prizeint = responseb , prize = responsec )
    else:
        return render_template('index.html', prizestring = 'empty', prizeint = 'empty', prize = 'empty' )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)