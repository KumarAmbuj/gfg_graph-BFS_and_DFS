from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def finddfs(self,u,vis):
        vis[u]=True
        print(u)
        for x in self.graph[u]:
            if vis[x]==False:
                self.finddfs(x,vis)

    def dfs(self,u):
        vis=[False for i in range(4)]

        self.finddfs(u,vis)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.dfs(1)