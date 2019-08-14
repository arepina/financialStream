import json

import requests
from flask import Flask, request
from flask_cors import CORS

from endpoints import *

app = Flask(__name__)
CORS(app)


def json_response(payload, status=200):
    return (json.dumps(payload), status, {'content-type': 'application/json'})


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


@app.route('/average', methods=["POST"])
def average():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AVERAGE,
                        json={"start": start, "end": end})
    # '[["an", "\\u00a3 321.00", null], ["en", null, "\\u00a3 743.00"], ["in", "\\u00a3 3,416.00", null], ["un", null, "\\u00a3 123.00"]]'
    averageBuy = []
    averageSell = []
    for item in resp.text.split('], ['):
        item = item.replace('[', '').replace(']', '').replace('\\u00a3', '')
        item = item[item.index(',') + 2:]
        sep = item.index(', ')
        buy = item[:sep].replace(" ", '').replace("\"", "")
        sell = item[sep + 2:].replace(" ", '').replace("\"", "")
        if buy == 'null':
            averageBuy.append(0)
        else:
            averageBuy.append(float(buy.replace(',', '')))
        if sell == 'null':
            averageSell.append(0)
        else:
            averageSell.append(float(sell.replace(',', '')))
    return json_response({'averageBuy': averageBuy, 'averageSell': averageSell})


@app.route('/dealers_position', methods=["POST"])
def dealers_position():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(DEALERS_POSITION,
                        json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/dealer_position', methods=["POST"])
def dealer_position():
    login = request.json['login']
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(DEALER_POSITION,
                        json={"login": login, "start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/realised_profit_loss_dealers', methods=["POST"])
def realised_profit_loss_dealers():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(REALISED_DEALERS, json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/realised_profit_loss_dealer', methods=["POST"])
def realised_profit_loss_dealer():
    login = request.json['login']
    date = request.json['date']
    resp = requests.get(REALISED_DEALER,
                        json={"login": login, "date": date})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/effective_profit_loss_dealers', methods=["POST"])
def effective_profit_loss_dealers():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(EFFECTIVE_DEALERS, json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/effective_profit_loss_dealer', methods=["POST"])
def effective_profit_loss_dealer():
    login = request.json['login']
    resp = requests.get(EFFECTIVE_DEALER,
                        json={"login": login})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_ending', methods=["POST"])
def aggregated_ending():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_ENDING, json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_effective', methods=["POST"])
def aggregated_effective():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_EFFECTIVE, json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/aggregated_realised', methods=["POST"])
def aggregated_realised():
    start = request.json['start']
    end = request.json['end']
    resp = requests.get(AGGREGATED_REALISED, json={"start": start, "end": end})
    return resp.text, resp.status_code, resp.headers.items()


@app.route('/get_stream_data', methods=["POST"])
def get_stream_data():
    resp = requests.get(GET_STREAM_DATA)
    return resp.text, resp.status_code, resp.headers.items()


def bootapp():
    app.run(port=PORT, threaded=True, host=HOST, debug=True)


if __name__ == '__main__':
    bootapp()
