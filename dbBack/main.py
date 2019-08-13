from flask import Flask, render_template, request
import pymysql
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


class Database:
    def __init__(self):
        host = "192.168.99.100"
        user = "root"
        password = "ppp"
        db = "mydata"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db)
        self.cur = self.con.cursor()

    def login(self, login, password, user_type):
        self.cur.execute(
            "INSERT INTO `USER`(`login`, `password`, `user_type`) "
            "VALUES ('{0}', '{1}', '{2}')".format(login, password, user_type))
        self.con.commit()

    def sign_up(self, login, password):
        self.cur.execute("SELECT * FROM `USER` "
                         "WHERE `login` = '{0}' and `password` = '{1}'".format(login, password))
        result = self.cur.fetchall()
        return result

    def average(self, type, start, end):
        self.cur.execute(
            "SELECT i.instr_name, avg(d.price)"
            "FROM DEAL d INNER JOIN INSTRUMENT i ON d.instrument_id = i.instrument_id"
            "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}' AND d.type = '{2}'"
            "GROUP BY i.instr_name;".format(start, end, type))
        result = self.cur.fetchall()
        return result

    def dealers_position(self, start, end):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity END) AS dealer_revenue"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}'"
                         "GROUP BY c.cpty_name;".format(start, end))
        result = self.cur.fetchall()
        return result

    def dealer_position(self, login, start, end):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}' AND d.timestamp > '{1}' AND d.timestamp <= '{2}'"
                         "GROUP BY c.cpty_name;".format(login, start, end))
        result = self.cur.fetchall()
        return result

    def realised_profit_loss_dealers(self, date):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '%{0}%'"
                         "GROUP BY c.cpty_name;".format(date))
        result = self.cur.fetchall()
        return result

    def realised_profit_loss_dealer(self, date, login):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE "
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}' AND d.timestamp > '%{1}%'"
                         "GROUP BY c.cpty_name;".format(login, date))
        result = self.cur.fetchall()
        return result

    def effective_profit_loss_dealers(self):
        self.cur.execute("SELECT c.cpty_name, "
                         "SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "GROUP BY c.cpty_name;")
        result = self.cur.fetchall()
        return result

    def effective_profit_loss_dealer(self, login):
        self.cur.execute("SELECT c.cpty_name,"
                         "SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}'"
                         "GROUP BY c.cpty_name;".format(login))
        result = self.cur.fetchall()
        return result

    def aggregated_ending(self, start, end):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '{0}' AND d.timestamp <= '{1}';".format(start, end))
        result = self.cur.fetchall()
        return result

    def aggregated_effective(self, date):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE d.timestamp > '%{0}%';".format(date))
        result = self.cur.fetchall()
        return result

    def aggregated_realised(self):
        self.cur.execute("SELECT SUM(CASE"
                         "WHEN d.type = 'B' THEN -d.price*d.quantity"
                         "WHEN d.type = 'S' THEN d.price*d.quantity"
                         "END) AS rev"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id;")
        result = self.cur.fetchall()
        return result

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





if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)
