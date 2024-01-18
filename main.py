# Flask testing

import flask
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# A list to store names
names = []


@app.route('/')
def index():
    return flask.render_template('index.html')


# Endpoint to handle PUT request for setting a name
@app.route('/set_name', methods=['POST'])
def set_name():
    # Get the name from the JSON payload
    data = request.json
    user_name = data.get('name')
    return jsonify({'names': user_name})


@app.route('/get_names', methods=['GET'])
def get_names():
    # Return the list of names
    return jsonify({'names': names})


def get_name(url):
    response = requests.get(url)

    data = response.json()

    name_list = data.get("names", [])
    print("Names:", names)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=1000)

    get_name('http://127.0.0.1:1000/get_names')
