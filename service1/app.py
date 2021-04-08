from flask import Flask, request, render_template
import requests
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        responsea = str(requests.get('service2/createletter'))
        responseb = str(requests.get('service3/createnumber'))
        responsec = str(requests.post('service4/getprize/'+ responseb + responsea))
        return render_template('index.html', prizestring = responsea, prizeint = responseb , prize = responsec )
    else:
        return render_template('index.html', prizestring = 'empty', prizeint = 'empty', prize = 'empty' )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001,debug=True)