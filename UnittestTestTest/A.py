# import os
# from pickle import *
from DumpUnitTest import *

MAX_NR = 100
isPickle = True


# def testPickleWriter(inObject):
#     if isPickle:
#         for k in inObject.keys():
#             for i in range(MAX_NR):
#                 pickleFile = 'dumps/' + k + '_' + str(i) + '.pickle'
#                 if not os.path.isfile(pickleFile):
#                     with open(pickleFile, 'w') as f:
#                         dump(inObject, f, HIGHEST_PROTOCOL)
#                     break


# class TestPickler(Pickler):
#     def __init__(self, inFileName):
#         if isPickle:
#             for i in range(MAX_NR):
#                 pickleFile = 'dumps/' + inFileName + '_' + str(i) + '.pickle'
#                 if not os.path.isfile(pickleFile):
#                     f = open(pickleFile, 'w')
#                     Pickler.__init__(self, f, HIGHEST_PROTOCOL)
#                     break


# ----------------------------------

class testPoint:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.properties = [x, y]

    def __eq__(self, other):
        return True if self.x == other.y and \
                       self.y == other.y else False


class TestLine(object):
    def __init__(self, x1, y1, x2, y2):
        self.p1 = testPoint(x1, y1)
        self.p2 = testPoint(y2, y2)
        self.x = x2-x1
        self.y = y2-y1
        self.manhattanLength = self.x + self.y


class TestVector(TestLine):
    #FIXME to check with method with multiple result
    #FIXME to have a loop relation
    @dumpUnitTestWriter(isON=True)
    def __init__(self, x, y):
        super(TestVector, self).__init__(0, x, 0, y)

    def __add__(self, other):
        res = TestVector()
        res.x = self.x + other.x
        res.y = self.y + other.y
        return res

    def __eq__(self, other):
        if isinstance (other, TestVector):
            return self.__dict__ == other.__dict__
        else:
            return False


def parametrizableDecorator(decoratorName):
    def testDec(*a):
        def w(f):
            return decoratorName(f, *a)
        return w
    return testDec

