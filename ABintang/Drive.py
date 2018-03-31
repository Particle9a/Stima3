import Graph
import heapq
import Tree
import copy


class PriorityQueue :
    def __init__(self):
        self.list = []
    def isEmpty(self):
        return(self.list == [])
    def push(self, elmt, prior):
        heapq.heappush(self.list, (prior,elmt))
    def pop(self):
        return(heapq.heappop(self.list)[1])

def aStar(Gstart,Ggoal) :
    queueG = PriorityQueue()
    cost = Gstart.getDistance(Ggoal)
    path = []
    G = (Gstart,path)
    T = Tree.Tree((G[0],cost))
    while G[0].value != Ggoal.value :
        for GG in G[0].getConnections() :
            cost = GG.getDistance(G[0]) + GG.getDistance(Ggoal)
            queueG.push((GG,path),cost)
            T.addPath((GG,cost),path)
        G = queueG.pop()
        path.append(G)
    return T

def aBintang(Gstart, Ggoal) :
    queueG = PriorityQueue()
    cost = Gstart.getDistance(Ggoal)
    path = []
    T = Tree.Tree((Gstart,path,cost))
    TT = T
    while T.value[0].value != Ggoal.value :
        for GG in T.value[0].getConnections() :
            cost = GG.getDistance(T.value[0]) + GG.getDistance(Ggoal)
            Ttemp = Tree.Tree((GG,path,cost))
            queueG.push(Ttemp, cost)
            T.addChildTr(Ttemp)
        T = queueG.pop()
        path = copy.deepcopy(T.value[1])
        path.append(T.value[0])
    return TT


def aStarSolve(Ggoal, queueG, prvCost):
    G = queueG.pop()
    if G[0].value == Ggoal.value:
        return Tree.Tree(Ggoal)
    else:
        cost = G.getDistance(Ggoal) + prvCost
        for GG in G.getConnections() :
            queueG.push()

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
mtk = makeMatrix("venv/mat.txt")
lS = makeList("venv/test.txt")
lG = []
G = Graph.Graph(lS,lG)
print(lG)
T = aBintang(lG[0], lG[6])
print(T)
