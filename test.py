from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Do you love me?? <a href="/yes"> <button type="button">Yes</ button> </a> <a href="/no"> <button type="button">No</ button> </a>'

@app.route('/no')
def no():
    return 'fuck you try again <a href="/"> <button type="button">Try Again</ button> </a>'

@app.route('/yes')
def yes():
    return 'Goooood Girllll'