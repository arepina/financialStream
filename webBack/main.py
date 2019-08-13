import requests
from flask import Flask, request
from flask_cors import CORS

from endpoints import CREATE_USER, GET_USER, GET_STREAM_DATA, AVERAGE, DEALERS_POSITION, DEALER_POSITION, \
    REALISED_DEALERS, REALISED_DEALER, EFFECTIVE_DEALERS, EFFECTIVE_DEALER, AGGREGATED_ENDING, AGGREGATED_REALISED, \
    AGGREGATED_EFFECTIVE

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


@app.route('/average', methods=["GET"])
def average():
    type = request.json['type']
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AVERAGE,
                        json={"type": type, "start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/dealers_position', methods=["GET"])
def dealers_position():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(DEALERS_POSITION,
                        json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/dealer_position', methods=["GET"])
def dealer_position():
    login = request.json['login']
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(DEALER_POSITION,
                        json={"login": login, "start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/realised_profit_loss_dealers', methods=["GET"])
def realised_profit_loss_dealers():
    date = request.json['date']
    resp = requests.get(REALISED_DEALERS,
                        json={"date": date})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/realised_profit_loss_dealer', methods=["GET"])
def realised_profit_loss_dealer():
    login = request.json['login']
    date = request.json['date']
    resp = requests.get(REALISED_DEALER,
                        json={"login": login, "date": date})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/effective_profit_loss_dealers', methods=["GET"])
def effective_profit_loss_dealers():
    resp = requests.get(EFFECTIVE_DEALERS)
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/effective_profit_loss_dealer', methods=["GET"])
def effective_profit_loss_dealer():
    login = request.json['login']
    resp = requests.get(EFFECTIVE_DEALER,
                        json={"login": login})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_ending', methods=["GET"])
def aggregated_ending():
    login = request.json['login']
    password = request.json['password']
    resp = requests.get(AGGREGATED_ENDING,
                        json={"login": login, "password": password})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_effective', methods=["GET"])
def aggregated_effective():
    date = request.json['date']
    resp = requests.get(AGGREGATED_EFFECTIVE,
                        json={"date": date})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_realised', methods=["GET"])
def aggregated_realised():
    resp = requests.get(AGGREGATED_REALISED)
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/get_stream_data', methods=["GET"])
def get_stream_data():
    resp = requests.get(GET_STREAM_DATA)
    return resp.text, resp.status_code, resp.headers.items()


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=5000)
