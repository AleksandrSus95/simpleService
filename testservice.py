from crypt import methods
from flask import Flask, render_template, request, jsonify
from num2words import num2words
import os

app = Flask(__name__)

@app.route('/num2text', methods=['POST',])
def num_text():
    json_data = request.get_json()
    if 'number' not in json_data:
        return jsonify(str='The key must be number')
    number = json_data['number']
    text = num2words(number, lang='ru')
    return jsonify(str=text)

@app.route('/', methods=['GET',])
def req_get():
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))