from flask import Flask, render_template, request
import pymysql
import json

from randomDealData import RandomDealData

app = Flask(__name__)


@app.route('/create_user', methods=['POST'])
def create_user():
    login = request.json.get('login')
    password = request.json.get('password')
    user_type = request.json.get('userType')
    try:
        db = Database()
        db.login(login, password, user_type)
        return app.response_class(
            response=json.dumps('OK'),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )


@app.route('/get_user', methods=['GET'])
def get_user():
    login = request.json.get('login')
    password = request.json.get('password')
    try:
        db = Database()
        data = db.sign_up(login, password)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )


@app.route('/average', methods=['GET'])
def average():
    type = request.json.get('type')  # buy(B) or sell(S)
    start = request.json.get('start')
    end = request.json.get('end')
    try:
        db = Database()
        data = db.average(type, start, end)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response

@app.route('/dealers_position', methods=['GET'])
def dealers_position():
    try:
        db = Database()
        data = db.dealers_position()
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


@app.route('/dealer_position', methods=['GET'])
def dealer_position():
    login = request.json.get('login')
    try:
        db = Database()
        data = db.dealer_position(login)
        return app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
