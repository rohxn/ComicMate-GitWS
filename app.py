from flask import Flask
from flask import request, jsonify, render_template
import os
import json

# Home page route With cards
# Comic page 

app = Flask(__name__)

@app.route('/')
def test():
    path = 'data/'
    files = os.listdir(path)
    result = []
    for file in files:
        with open("data/"+file, 'r') as f:
            result.append(json.load(f))
    print(result)
    return "Hello akshay"

@app.route('/'):

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1233)
