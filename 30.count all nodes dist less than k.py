from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis,c,k,hash):
        if c>=k:
            return

        if c>0 and c<k:
            hash.add(u)

        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis,c+1,k,hash)
        vis[u]=False



    def findlessdist(self,marked):
        vis=[False for i in range(self.v)]
        k=3
        hash=set()
        for u in marked:
            self.dfs(u,vis,0,k,hash)
        print(len(hash))

g=Graph(10)

g.addEdge(1,0)
g.addEdge(0,3)
g.addEdge(0,8)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(3,6)
g.addEdge(3,7)
g.addEdge(4,5)
g.addEdge(5,9)
marked = [1, 2, 4]
g.findlessdist(marked)

