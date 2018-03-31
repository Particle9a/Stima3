import copy
import math

class Tree :

    def __init__(self, X, lC = None):
        self.value = X
        self.children = lC

    def addChild(self, X):
        if self.children == None :
            self.children = [Tree(X)]
            return
        self.children.append(Tree(X))
    def addChildTr(self,X):
        if self.children == None :
            self.children = [X]
            return
        self.children.append(X)

    def addChildPath(self,X,listP):
        if listP == [] :
            self.addChildTr(X)
        else :
            G = listP.pop(0)
            for child in self.children :
                if child.value[0].value == G[0].value :
                    child.addChildPath(X,listP)
                    break


    def addPath(self, X, listP):
        print(X)
        print(listP)
        if listP == [] :
            self.addChild(X)
        else :
            G = listP.pop(0)
            for child in self.children :
                if child.value[0].value == G[0].value :
                    child.addPath(X,listP)
                    break

    def addChildOn(self,X, val, n):
        if (n == 0) :
            if(self.value == val):
                self.addChild(X)
                return True
            else :
                return False
        elif (self.children == None):
            return False
        else :
            for child in self.children :
                if child.addChildOn(X,val,n - 1) :
                    return True
            return False
    def toStr(self,a):
        S = str(self.value[0]) + " " + str(self.value[2])
        if (self.children == None):
            return S
        else :
            for child in self.children :
                S += "\n"
                for i in range(0,a):
                    S += " "
                S += child.toStr(a +1)
            return S
    def __repr__(self):
        return self.toStr(1)
    def __lt__(self, other):
        return self.value[2] < other.value[2]
    def __gt__(self,other):
        return self.value[2] > other.value[2]