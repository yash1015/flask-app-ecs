from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Yash Here , welcome     Thanks     welcome again'

@app.route('/health')
def health():
    return 'Server is up and running'
