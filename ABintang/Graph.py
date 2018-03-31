import matplotlib
import copy
import math

class Graph :
    def __init__(self, listStr, listGrph):
        self.connections = []
        if(listStr == []):
            self = None
        elif (listStr[0] == []):
            listStr.pop(0)
            self = Graph(listStr, listGrph)
        elif (listStr[0][0] == []) :
            listStr[0].pop(0)
            self = Graph(listStr,listGrph)
        else:
            self.value = listStr[0][0]
            self.coordinate = (listStr[0][1], listStr[0][2])
            listGrph.append(self)
            for i in range(3,len(listStr[0])):
                xs = next((x for x in listGrph if x.value == listStr[0][i]), None)
                if(xs != None):
                    self.connections.append(xs)
                else:
                    listStr2 = copy.deepcopy(listStr)
                    listStr2.pop(0)
                    a  = [x[0] for x in listStr2].index(listStr[0][i])
                    listStr2[a], listStr2[0] = listStr2[0], listStr2[a]
                    self.connections.append(Graph(listStr2,listGrph))
    def getConnections(self):
        return self.connections
    def getDistance(self, G):
        sx, sy = self.coordinate
        gx, gy = G.coordinate
        x = (sx - gx)**2
        y = (sy - gy)**2
        return(math.sqrt(x + y))
    def __repr__(self):
        return(self.value)
    def __str__(self):
        return self.value
