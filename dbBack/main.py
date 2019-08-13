import json

from flask import Flask, request
from flask_cors import CORS

from Database import Database
from endpoints import PORT, HOST

app = Flask(__name__)
CORS(app)


@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        login = request.json.get('login')
        password = request.json.get('password')
        user_type = request.json.get('userType')
        db = Database()
        db.sign_up(login, password, user_type)
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
    try:
        login = request.json.get('login')
        password = request.json.get('password')
        db = Database()
        data = db.login(login, password)
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
    try:
        type = request.json.get('type')  # buy(B) or sell(S)
        start = request.json.get('start')
        end = request.json.get('end')
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
    try:
        login = request.json.get('login')
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


@app.route('/realised_profit_loss_dealers', methods=['GET'])
def realised_profit_loss_dealers():
    try:
        date = request.json.get('date')
        db = Database()
        data = db.realised_profit_loss_dealers(date)
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


@app.route('/realised_profit_loss_dealer', methods=['GET'])
def realised_profit_loss_dealer():
    try:
        login = request.json.get('login')
        date = request.json.get('date')
        db = Database()
        data = db.realised_profit_loss_dealer(date, login)
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


@app.route('/effective_profit_loss_dealers', methods=['GET'])
def effective_profit_loss_dealers():
    try:
        db = Database()
        data = db.effective_profit_loss_dealers()
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


@app.route('/effective_profit_loss_dealer', methods=['GET'])
def effective_profit_loss_dealer():
    try:
        login = request.json.get('login')
        db = Database()
        data = db.effective_profit_loss_dealer(login)
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


@app.route('/aggregated_ending', methods=['GET'])
def aggregated_ending():
    try:
        start = request.json.get('start')
        end = request.json.get('end')
        db = Database()
        data = db.aggregated_ending(start, end)
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


@app.route('/aggregated_effective', methods=['GET'])
def aggregated_effective():
    try:
        date = request.json.get('date')
        db = Database()
        data = db.aggregated_effective(date)
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


@app.route('/aggregated_realised', methods=['GET'])
def aggregated_realised():
    try:
        db = Database()
        data = db.aggregated_realised()
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


@app.route('/add_stream_data', methods=['GET', 'POST'])
def add_stream_data():
    try:
        instrumentName = request.json.get("instrumentName")
        cpty = request.json.get("cpty")
        price = request.json.get("price")
        type = request.json.get("type")
        quantity = request.json.get("quantity")
        time = request.json.get("time")
        db = Database()
        data = db.add_stream_data(instrumentName, cpty, price, type, quantity, time)
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


@app.route('/get_stream_data', methods=['GET'])
def get_stream_data():
    try:
        db = Database()
        data = db.get_stream_data()
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


def bootapp():
    app.run(port=PORT, threaded=True, host=HOST)


if __name__ == '__main__':
    bootapp()
