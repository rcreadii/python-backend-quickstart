from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, our World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/api')
def api():
    return 'Api page'