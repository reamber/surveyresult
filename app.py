from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def lyft():
    if request.method == 'POST':
        data = request.get_json()
        output = ""
        if data is not None:
            for enum, character in enumerate(list(data['string_to_cut'])):
                if enum%3 == 2:
                    output += character
        return jsonify({"return_string": output})
