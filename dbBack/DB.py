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
            "SELECT i.instr_name, avg(d.price) "
            "FROM `DEAL` d INNER JOIN `INSTRUMENT` i "
            "ON d.instrument_id = i.instrument_id "
            "WHERE timestamp > '{0}' AND timestamp < '{1}' AND type = '{2}'"
            "GROUP BY i.instr_name;".format(start, end, type))
        result = self.cur.fetchall()
        return result

    def dealers_position(self):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "GROUP BY c.cpty_name;")
        result = self.cur.fetchall()
        return result

    def dealer_position(self, login):
        self.cur.execute("SELECT c.cpty_name, sum(d.price*d.quantity)"
                         "FROM DEAL d INNER JOIN COUNTER_PARTY c ON d.counter_party_id = c.counter_party_id"
                         "WHERE c.cpty_name = '{0}'"
                         "GROUP BY c.cpty_name;".format(login))
        result = self.cur.fetchall()
        return result
