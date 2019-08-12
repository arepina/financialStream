from flask import Flask, render_template, request
import pymysql
import json

from randomDealData import RandomDealData

app = Flask(__name__)

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
            "INSERT INTO `USER`(`login`, `password`, `user_type`) VALUES ('{0}', '{1}', '{2}')".format(login, password, user_type))
        self.con.commit()

    def sign_up(self, login, password):
        self.cur.execute("SELECT * FROM `USER` WHERE `login` = '{0}' and `password` = '{1}'".format(login, password))
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
        response = app.response_class(
            response=json.dumps('OK'),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response

@app.route('/get_user', methods=['GET'])
def get_user():
    login = request.json.get('login')
    password = request.json.get('password')
    try:
        db = Database()
        data = db.sign_up(login, password)
        response = app.response_class(
            response=json.dumps(data),
            status=200,
            mimetype='application/json'
        )
        return response
    except Exception as e:
        response = app.response_class(
            response=json.dumps(e),
            status=400,
            mimetype='application/json'
        )
        return response


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=80)