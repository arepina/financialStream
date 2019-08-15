from Database import Database

class Test_Database:

    def test_add_stream_data(self):
        instrumentName = "Galactia"
        cpty = "Lewis"
        price = 12345
        type = "S"
        quantity = 2
        time = "11-Aug-2019 (12:07:07.042573)"
        result = Database.add_stream_data(self, instrumentName, cpty, price, type, quantity, time)





