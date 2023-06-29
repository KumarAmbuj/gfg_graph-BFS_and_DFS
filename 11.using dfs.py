from collections import defaultdict


class Graph:
    def __init__(self,v):
        self.graph=defaultdict(list)
        self.v=v

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,level,vis,count,n):
        vis[u]=True
        if n==level:
            count[0]+=1

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,level,vis,count,n+1)


    def findlevel(self,u,level):
        count=[0]
        vis=[False for i in range(self.v)]

        self.dfs(u,level,vis,count,0)
        print(count[0])


g=Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)

level = 2

g.findlevel(0,level)



