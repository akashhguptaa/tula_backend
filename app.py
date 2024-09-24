from flask import Flask, url_for, jsonify
from conversation import speech_to_text, text_to_speech

app = Flask(__name__)

@app.route('/')
def home():
    return "hello world"

@app.route('/mic', methods = ['GET', 'POST'])
def microphone_response():
    
@app.route('/video')


