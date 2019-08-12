from instrument import Instrument


class Test_instrument:

    def test_init(self):
        name = "Myname"
        base = 10
        drift = 3
        variance = 2
        testobject = Instrument(name, base, drift, variance)
        assert testobject.name == name


tester = Test_instrument()
tester.test_init()
