from flask import Flask, Response, requests, request
import functools


app = Flask(__name__)

@app.route('/register', methods=('POST'))
def register():
    username = request.form['username']
    password = request.form['password']
    userType = request.form['type']
    
    r = requests.get("")
    return Response(
            r.text,
            status=r.status_code,
            content_type=r.headers['content_type'],)



@app.route('/login', methods=('GET'))
def login():
    username = request.form['username']
    password = request.form['password']
    
    r = requests.get("")
    return Response(
            r.text,
            status=r.status_code,
            content_type=r.headers['content_type'],)


if __name__ == "__main__":
    app.run(debug=True)
