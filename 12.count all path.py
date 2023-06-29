from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,u,dest,vis,count):
        if u==dest:
            count[0]+=1
            return

        vis[u]=True
        for v in self.graph[u]:
            if vis[v]==False:

                self.dfs(v,dest,vis,count)

        vis[u]=False



    def findcount(self,src,dest):
        vis=[False for i in range(self.v)]
        count=[0]

        self.dfs(src,dest,vis,count)
        print(count[0])


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(1, 3)

s = 2
d = 3
g.findcount(s,d)