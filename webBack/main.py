import requests
from flask import Flask, Response, request

from endpoints import CREATE_USER, GET_USER

app = Flask(__name__)


@app.route('/register', methods=["POST"])
def register():
    username = request.form['username']
    password = request.form['password']
    userType = request.form['type']
    r = requests.post(CREATE_USER,
                      json={"username": username, "password": password, "userType": userType})
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content_type'], )


@app.route('/login', methods=["GET"])
def login():
    username = request.form['username']
    password = request.form['password']
    r = requests.get(GET_USER,
                     json={"username": username, "password": password})
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content_type'], )


if __name__ == "__main__":
    app.run(debug=True)
