from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests, random, string, os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_string = db.Column(db.String(30), nullable=False)
    account_int = db.Column(db.String(30), nullable=False)
    prize = db.Column(db.Integer, nullable=False)

db.create_all()

def addToDB(accountstring,accountint,accountprize):
    account = Account(account_string = accountstring, account_int = accountint, prize = accountprize)
    db.session.add(account)
    db.session.commit()
    return


@app.route('/', methods=['GET','POST'])
def index():
    #accounts = Account.query.all()
    if request.method == 'POST':
        responsea = requests.get('http://service2:5002/createletters').text
        responseb = requests.get('http://service3:5003/createnumber').text
        responsec = requests.post('http://service4:5004/getprize/'+ responsea + responseb).text
        addToDB(responsea,responseb,responsec)
        return render_template('index.html', accountlist = accounts, prizestring = responsea, prizeint = responseb , prize = responsec )
    else:
        return render_template('index.html', accountlist = accounts, prizestring = 'empty', prizeint = 'empty', prize = 'empty' )


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)