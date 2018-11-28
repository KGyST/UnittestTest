from unittest import TestCase
import jsonpickle

class TestCClass(TestCase):
    def test(self):
        for li in jsonList:
            self.assertEqual(jsonpickle.decode(li)['a1'] + jsonpickle.decode(li)['a2'], jsonpickle.decode(li)['c1'])

    def setUp(self):
        global jsonList
        with open('dumps/teszt.json', 'r') as jsonFile:
            jsonList = jsonpickle.decode(jsonFile.read())

