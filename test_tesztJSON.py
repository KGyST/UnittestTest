from unittest import TestCase, TestSuite
import jsonpickle
from A import TesztJSON as tj
import os

class SuiteTesztJSON(TestSuite):
    def __init__(self):
        self._tests = []
        dir_prefix = 'testTests\\testTest'
        dirName = dir_prefix + '_items'
        for f in os.listdir(dirName):
            if os.path.isfile(dir + "\\" + f) and f[0] != '_':
                print f
                tp = TestTesztJSON(f, dir_prefix)
                self.addTest(tp)
        super(SuiteTesztJSON, self).__init__(self._tests)


class TestTesztJSON(TestCase):
    def __init__(self, inFile, inDirPrefix):
        func = self.ParamTestCaseFactory(inFile, inDirPrefix)
        setattr(TestTesztJSON, func.__name__, func)
        super(TestTesztJSON, self).__init__(func.__name__)

    @staticmethod
    def ParamTestCaseFactory(inFileName, inDirPrefix):
        def func(inObj):
            with open(inDirPrefix + "_items" + "\\" + inFileName, "r") as testFile:
                testNode = testFile.read()
                par = Param(inETree=etree.XML(testNode))
                out_file_name = inDirPrefix + "_errors\\" + inFileName
                if os.path.isfile(out_file_name):
                    os.remove(out_file_name)
                try:
                    inObj.assertEqual(testNode, etree.tostring(par.eTree))
                except AssertionError:
                    with open(out_file_name, "w") as of:
                        of.write(etree.tostring(par.eTree))
                    raise

        func.__name__ = "test_" + inFileName[:-4]
        return func


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

