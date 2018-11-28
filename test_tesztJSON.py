from unittest import TestCase
import jsonpickle
from A import TesztJSON as tj


class TestTesztJSON(TestCase):
    # def test_readFromFile(self):
    #     self.fail()
    #
    # def test_writeToFile(self):
    #     self.fail()
    #
    # def test_insert(self):
    #     self.fail()
    #
    # def test_delete(self):
    #     self.fail()
    #
    # def test_navigate(self):
    #     self.fail()
    #
    # def test_isNodeEmpty(self):
    #     self.fail()

    def test_removeJSONStructure(self):
        for li in rem_list:
            print li["name"]
            t = tj("")
            t.JSONDict = li['full']
            t._removeNode(li['template'], t.JSONDict)
            self.assertEqual(t.JSONDict, li['result'])

    # def test_addJSONStructure(self):
    #     self.fail()

    def setUp(self):
        global rem_list
        with open('dumps/tesztTeszt.json', 'r') as jsonFile:
            jsonDict = jsonpickle.decode(jsonFile.read())
            rem_list = jsonDict['removeJSONStructure']

