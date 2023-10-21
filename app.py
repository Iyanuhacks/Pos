from flask import Flask, render_template
from flask_frozen import Freezer
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/power/power.html')
def power():
  return render_template("power.html")

@app.route('/anime/anime.html')
def anime():
  return render_template("anime.html")

@app.route('/loading/loading',methods=['POST'])
def loading():
  return render_template("loading.html")

@app.template_filter('timeformat2')
def timeformat2(s):
    return time.strftime('%S', time.gmtime(s))


@app.template_filter('timeformat')
def timeformat(s):
    return time.strftime('%M:%S', time.gmtime(s))

@app.route('/index') #,methods=['POST'])
def index():
    account_name = generate_account_name()
    account_number = generate_account_number()
    bank_name = generate_bank_name()
    return render_template('index.html', name=account_name, number=account_number, bank=bank_name)

def generate_account_name():
    name = "Winning Ogunleye"
    return name

def generate_account_number():
    number = "8169550766"
    return number

def generate_bank_name():
    bank = "Palmpay"
    return bank

freezer = Freezer(app)


if __name__ == '__main__':
#    freezer.freeze()
    app.run(debug=False)

