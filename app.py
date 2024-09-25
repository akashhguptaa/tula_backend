from flask import Flask, url_for, jsonify, request, Response
from conversation import speech_to_text, text_to_speech

app = Flask(__name__)

def AI_MODEL():
    return None

@app.route('/')
def home():
    return "hello world"

@app.route('/mic', methods = ['GET', 'POST'])
def microphone_response():
    if request.method == "POST":
        text = speech_to_text()
        print(text)
        AI_MODEL(text)
        return jsonify({"status": "done", "text": text}), 200
      
    elif request.method == "GET":
        data = request.get_json()
        text = request.get('text')
        text_to_speech(text)
        AI_MODEL(text)
        return jsonify({"status": "done", "text": text}), 200
        
              

@app.route('/video', methods = ['GET', 'POST'])
def video_response():




