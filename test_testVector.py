from unittest import TestCase
import os
import jsonpickle
from A import TestVector

class TestTestVector(TestCase):
    def test___init__(self):
        JSONDir = 'dumps'
        JSONFile = 'test'
        iDecimals = 3
        funcName = '__init__'

        iFile = 1
        try:
            while True:
                JSONFileName = JSONDir + '\\' + funcName + "_" + JSONFile + '_' + str(iFile).zfill(iDecimals) + '.json'
                if os.path.isfile(JSONFileName):
                    with open(JSONFileName, "r") as f:
                        jsonDict = jsonpickle.decode(f.read())
                        if jsonDict['root'][0]['isON']:
                            print jsonDict['root'][0]['name']
                            args = jsonDict['root'][1]['list']
                            kwargs = jsonDict['root'][1]['dict']
                            kwargs['isON'] = False
                            res = jsonDict['root'][2]['result']

                            self.assertEqual(TestVector.__init__(*args, **kwargs), res)
                    iFile += 1
                else:
                    break
        except AssertionError:
            raise
        #FIXME

