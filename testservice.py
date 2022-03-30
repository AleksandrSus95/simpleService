from flask import Flask, request, jsonify
from num2words import num2words

app = Flask(__name__)

@app.route('/num2text/', methods=['POST'])
def num_text():
    json_data = request.get_json()
    if 'number' not in json_data:
        return jsonify(str='The key must be number')
    number = json_data['number']
    text = num2words(number, lang='ru')
    return jsonify(str=text)

if __name__=='__main__':
    app.run(debug=True)
