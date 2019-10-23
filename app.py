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
    colours = ['blue', 'red', 'green', 'orange', 'pink', 'yellow']
    for file in files:
        with open("data/"+file, 'r') as f:
            json_data = json.load(f)
            json_data['slug'] = file[:-5]
            result.append(json_data)
    print(result)
    return render_template('index.html', artists = result, colours = colours)


@app.route('/<name>')
def get_contents(name):
    try:
        with open(f"data/{name}.json", 'r') as f:
            return render_template("personal.html", artist = json.load(f))
    except:
        return jsonify({
            'msg': 'File not found',
            'success': False
        })

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=1233)
