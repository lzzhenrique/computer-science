from flask import Flask, jsonify, request, json


app = Flask(__name__)


@app.route('/')
def index():
    # GET
    return "blaaaaaa"


@app.route('/get', methods=['GET'])
def get():
    return jsonify(
        {"msg": "PArabens vc chamou a rota GET"})


@app.route('/post', methods=['POST'])
def post():
    data = json.loads(request.data)
    return jsonify({"msg": data})



# ➜ curl --request POST --header "Content-type: application/json" --header "node: bao demais" http://127.0.0.1:5000/header 

@app.route('/header', methods=['POST'])
def header():
    data = dict(request.headers)
    return data


if __name__ == '__main__':
    app.run(debug=True)
