from crypt import methods
from flask import Flask, request, jsonify
from num2words import num2words

app = Flask(__name__)

# @app.route('/num2text/', methods=['POST'])
# def num_text():
#     json_data = request.get_json()
#     if 'number' not in json_data:
#         return jsonify(str='The key must be number')
#     number = json_data['number']
#     text = num2words(number, lang='ru')
#     return jsonify(str=text)

# @app.route('/testget', methods=['GET'])
# def test_get():
#     return "hi i'm simple service"

@app.route('/test')
def test():
    return "hi i'm simple service"
    
if __name__=='__main__':
    app.run('0,0,0,0', port=9991)
