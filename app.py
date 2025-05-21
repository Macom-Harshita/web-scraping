from flask import Flask
import requests
from flask import render_template
from scraper.codeforces import get_codeforces_contests

app = Flask(__name__)

@app.route('/')
def home():
    codeforces =  get_codeforces_contests()
    return render_template('index.html', codeforces = codeforces)

if __name__ == '__main__':
    app.run(debug = True)
