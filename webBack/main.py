import requests
from flask import Flask, Response, request

from endpoints import CREATE_USER, GET_USER

app = Flask(__name__)


@app.route('/register', methods=["POST"])
def register():
    login = request.args['login']
    password = request.args['password']
    userType = request.args['userType']
    r = requests.post(CREATE_USER,
                      json={"login": login, "password": password, "userType": userType})
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content_type'], )


@app.route('/login', methods=["GET"])
def login():
    login = request.args['login']
    password = request.args['password']
    r = requests.get(GET_USER,
                     json={"login": login, "password": password})
    return Response(
        r.text,
        status=r.status_code,
        content_type=r.headers['content_type'], )


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
