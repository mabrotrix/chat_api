from flask import Flask,render_template,request,jsonify
from flask_cors import CORS,cross_origin
import json
import io
import requests
import json 
import numpy as np
from chat_bot import *
app = Flask(__name__)
CORS(app, origins="*", allow_headers="*", supports_credentials=True)

@app.route('/chat',methods = ['POST','GET'])
def get_bot_response():
    userText = request.json
    print(userText['msg'])
    return jsonify(message = 'sucess',response = chat(userText['msg']),status = 200)


if __name__ == "__main__":
    app.run()
