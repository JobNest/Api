import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    json_data = request.get_json()
    data = request.get_data()

    f = open('logs.txt', 'w')
    f.write(data)
    f.close()
    return jsonify(json_data)

@app.route('/search', methods=['POST'])
def search():
    json_data = request.get_json()
    data = request.get_data()

    f = open('search.txt', 'w')
    f.write(data)
    f.close()
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True)
