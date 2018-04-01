import Graph
import heapq
import Tree
import copy
import pylab
from matplotlib.pyplot import pause
import networkx as nx

class PriorityQueue :
    def __init__(self):
        self.list = []
    def isEmpty(self):
        return(self.list == [])
    def push(self, elmt, prior):
        heapq.heappush(self.list, (prior,elmt))
    def pop(self):
        return(heapq.heappop(self.list)[1])

# def aStar(Gstart,Ggoal) :
#     queueG = PriorityQueue()
#     cost = Gstart.getDistance(Ggoal)
#     path = []
#     G = (Gstart,path)
#     T = Tree.Tree((G[0],cost))
#     while G[0].value != Ggoal.value :
#         for GG in G[0].getConnections() :
#             cost = GG.getDistance(G[0]) + GG.getDistance(Ggoal)
#             queueG.push((GG,path),cost)
#             T.addPath((GG,cost),path)
#         G = queueG.pop()
#         path.append(G)
#     return T

def selectNodeC(G,s, l = [],chk = None) :
    lC = {} 
    for c in G.listValue :
        lC[c] = 1
    for c in l :
        lC[c] = 3
    lC[s] = 5
    if chk != None :
        lC[chk] = 4
    listColor = [lC.get(node, 0.25) for node in G.nodes()]
    return listColor

def aBintang(G,start, goal) :
    queueG = PriorityQueue()
    cost = G.getDistancePos(start,goal)
    path = []
    T = Tree.Tree((start,path,cost))
    draw(G,selectNodeC(G,start))
    TT = T
    while T.value[0] != goal :
        for sT in G.getConnections(T.value[0]) :
            if not(sT in T.value[1]) :
                cost = G.getDistance(T.value[0],sT) + G.getDistancePos(T.value[0], goal)
                Ttemp = Tree.Tree((sT,path,cost))
                queueG.push(Ttemp, cost)
                draw(G,selectNodeC(G,T.value[0],[start] + T.value[1],sT))
                T.addChildTr(Ttemp)
        T = queueG.pop()
        path = copy.deepcopy(T.value[1])
        path.append(T.value[0])
        draw(G,selectNodeC(G,T.value[0], [start] + T.value[1]))
    pathSol = [start] + T.value[1] + [goal]
    return (TT , pathSol)


# def aStarSolve(Ggoal, queueG, prvCost):
#     G = queueG.pop()
#     if G[0].value == Ggoal.value:
#         return Tree.Tree(Ggoal)
#     else:
#         cost = G.getDistance(Ggoal) + prvCost
#         for GG in G.getConnections() :
#             queueG.push()

def makeList(S) :
    fil = open(S, "r")
    content = fil.read()
    l1 = content.split("\n")
    lS = []
    for s in l1:
        l2 = s.split(" ")
        lS.append(l2)
    for ll in lS:
        ll[1] = int(ll[1])
        ll[2] = int(ll[2])
    return lS

def makeMatrix(S) :
    fil = open(S,"r")
    content = fil.read()
    l1 = content.split("\n")
    lS = []
    for s in l1:
        l2 = s.split(' ')
        lS.append(l2)
    for l1 in lS :
        for i in range(0,len(l1)):
            l1[i] = int(l1[i])
    return lS

def draw(G,lColor) :
    fig = pylab.figure()
    nx.draw(G, node_color=lColor,pos = nx.get_node_attributes(G,'Position'),with_labels = True)
    fig.canvas.draw()
    pylab.draw()
    pause(2)
    pylab.close(fig)

mtk = makeMatrix("venv/mat.txt")
lS = makeList("venv/test.txt")
# lG = []
G = Graph.Graph(lS,mtk)
pylab.ion()
print(G.listValue)
start = G.listValue[0] 
goal = G.listValue[4]
T, sol = aBintang(G, start,goal)
print(T)
print(sol)
dis = 0
for i in range (0, len(sol) - 1) :
    dis += G.getDistance(sol[i],sol[i+1])
print("Distance from " + start + " to " + goal + " = ", dis)
