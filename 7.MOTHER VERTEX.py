from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def dfs(self,u,vis):

        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)
    def findmothervertex(self):

        vis=[False for i in range(self.v)]

        v=-1
        for i in range(self.v):
            if vis[i]==False:
                self.dfs(i,vis)
                v=i


        vis=[False for i in range(self.v)]
        self.dfs(v,vis)

        for i in range(self.v):
            if vis[i]==False:
                print(-1)
                break
        else:
            print(v)

g = Graph(5)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(1, 0)
g.addEdge(2, 1)

g.addEdge(3, 4)
g.findmothervertex()
