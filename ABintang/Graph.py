import matplotlib
import copy
import math
import networkx as nx
import pylab
from matplotlib.pyplot import pause

pylab.ion()

class Graph(nx.Graph) :
    def __init__(self, lStr, mtrx):
        listStr = copy.deepcopy(lStr)
        self.listDistance = {}
        for s in lStr :
            self.listDistance[s[0]] = {}
        i = 0 
        for lM in mtrx :
            j = 0
            for mx in lM :
                self.listDistance[lStr[i][0]][lStr[j][0]] = mx
                j+= 1
            i+= 1
        i = 0
        self.listValue = []
        self.node_number = 0
        super(Graph,self).__init__()
        while(listStr != []):
            if (listStr[0] == []):
                listStr.pop(0)
            elif (listStr[0][0] == []) :
                listStr[0].pop(0)
            else:
                self.node_number += 1
                k = listStr[0][0]
                self.add_node(k, Position=(listStr[0][1], listStr[0][2]))
                self.listValue.append(listStr[0][0])
                listStr.pop(0)
                for s1 in lStr :
                    for s2 in lStr :
                        if (self.listDistance[s1[0]][s2[0]] != 0) :
                             self.add_edge(s1[0],s2[0])
    def getDistance(self, e1, e2) :
        return(self.listDistance[e1][e2])
    def getDistancePos(self, e1,e2) :
        lpos = nx.get_node_attributes(self,'Position')
        pos1 = lpos[e1]
        pos2 = lpos[e2]
        a = (pos1[0] - pos2[0]) * (pos1[0] - pos2[0])
        b = (pos1[1] - pos2[1]) * (pos1[1] - pos2[1])
        return math.sqrt(a + b)
    def getConnections(self,e1) :
        l = []
        for s in self.listValue :
            if self.listDistance[e1][s] != 0 :
                l.append(s)
        return(l)
    
        