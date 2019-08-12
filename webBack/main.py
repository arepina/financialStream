import requests
from flask import Flask, request
from flask_cors import CORS

from endpoints import CREATE_USER, GET_USER

app = Flask(__name__)
CORS(app)


@app.route('/register', methods=["POST"])
def register():
    login = request.json['login']
    password = request.json['password']
    userType = request.json['userType']
    resp = requests.post(CREATE_USER,
                         json={"login": login, "password": password, "userType": userType})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/login', methods=["POST"])
def login():
    login = request.json['login']
    password = request.json['password']
    resp = requests.get(GET_USER,
                        json={"login": login, "password": password})
    return resp.text, resp.status_code, resp.headers.items()


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
