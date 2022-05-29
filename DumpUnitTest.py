import os.path
import jsonpickle

MAX_NR = 100

class TesztJSON():
    def __init__(self, inFileName):
        self.file = inFileName
        if os.path.isfile(self.file):
            self.JSONDict = self.readFromFile()
        else:
            self.JSONDict = {"root": []}

    def readFromFile(self):
        with open(self.file, 'r') as jsonFile:
            self.JSONDict = jsonpickle.decode(jsonFile.read())

    def writeToFile(self):
        with open(self.file, 'w') as jsonFile:
            jsonFile.write(jsonpickle.encode(self.JSONDict))

    def insert(self, JSONStructure, inPos='root'):
        pos = self.navigate(inPos)
        if isinstance(pos[inPos], list):
            pos[inPos] += [JSONStructure]
        # elif isinstance(pos, dict): pos[]

    def delete(self, path):
        node = self.navigate(path)
        del node

    def navigate(self, pos):
        root = self.JSONDict
        path = pos.split("/")
        return self.__getNode(root, path)

    def __getNode(self, node, path):
        nextNode = path.pop()
        if not path:
            return node
        else:
            self.__getNode(node[nextNode], path)

    def isNodeEmpty(self, inNode):
        if isinstance(inNode, list):
            return False if len(inNode) else True
        elif isinstance(inNode, dict):
            return False if len(inNode.keys()) else True
        else:
            return True

    def removeJSONStructure(self, inJSONToRemove, inPos):
        with open(inJSONToRemove, "r") as jFile:
            selfNode = self.navigate(inPos)
            inNodeToRemove = jsonpickle.decode(jFile.read())
            self._removeNode(inNodeToRemove, selfNode)

    @staticmethod
    def __classesMatch(inElement, inFromNode):
        isMatch = False
        for j in inFromNode:
            if type(inElement) == type(j):
                isMatch = True
                break
        return isMatch

    def _removeNode(self, inChildToBeRemoved, inFromNode):
        if inChildToBeRemoved:
            if isinstance(inChildToBeRemoved, list):
                for i in inChildToBeRemoved:
                    for j in inFromNode:
                        if self._removeNode(i, j):
                            inFromNode.remove(j)
                            # FIXME not inFromNode sok helyen van
                if not inFromNode:
                    return True
            elif isinstance(inChildToBeRemoved, dict):
                for i in inChildToBeRemoved.keys():
                    if i in inFromNode:
                        if self._removeNode(inChildToBeRemoved[i], inFromNode[i]):
                            del inFromNode[i]
                if not inFromNode:
                    return True
            elif isinstance(inChildToBeRemoved, tuple):
                bLeaveHere = False
                for i in inChildToBeRemoved:
                    if i in inFromNode:
                        if not self._removeNode(inChildToBeRemoved[i], inFromNode[i]):
                            bLeaveHere = True
                    else:
                        if not self.__classesMatch(i, inFromNode):
                            bLeaveHere = True
                if not bLeaveHere:
                    return True
                if not inFromNode:
                    return True
            elif isinstance(inChildToBeRemoved, int):
                return True
            elif isinstance(inChildToBeRemoved, float):
                return True
            elif isinstance(inChildToBeRemoved, bool):
                return True
            elif isinstance(inChildToBeRemoved, str):
                return True
            else:
                pass    # FIXME basic types
            return False
        else:
            return True

    def addJSONStructure(self, inJSONToAdd, inPos):
        with open(inJSONToAdd, "r") as jFile:
            selfNode = self.navigate(inPos)
            inNodeToAdd = jsonpickle.decode(jFile.read())
            self.__addNode(inNodeToAdd, selfNode)

    def __addNode(self, inChildToBeAdded, inToNode):
        pass

    # def addJSONStructure(self, inJSON, inPos):
    #     pos = self.navigate(inPos)
    #     pass


def parametrized_decorator(decoratorName):
    def dec(*args, **kwargs):
        def wrapper(func):
            return decoratorName(func, *args, **kwargs)
        return wrapper
    return dec


@parametrized_decorator
def dumpUnitTestWriter(func,
                       JSONDir='dumps',
                       JSONFile='test',
                       iDecimals = 3,
                       JSONTemplate='fixture.json',
                       isON = False):
    def wrapper(*args, **kwargs):
        if 'isON' in kwargs:
            isON = kwargs['isON']
            del kwargs['isON']
        iFile = 1
        while True:
            #FIXME classname
            JSONFileName = JSONDir + '\\' + func.__name__ + "_" + JSONFile + '_' + str(iFile).zfill(iDecimals) + '.json'
            if not os.path.isfile(JSONFileName):
                break
            else:
                iFile += 1

        if isON:
            tJSON = TesztJSON(JSONFileName)
            tJSON.insert({"name": "", "isON": True})
            tJSON.insert({"list": args, "dict": kwargs}, 'root')

        result = func(*args, **kwargs)

        if isON:
            tJSON.insert({"result": result}, 'root')
            # tJSON.removeJSONStructure("dumps/fixture.json", "root")
            tJSON.writeToFile()
        return result

    return wrapper