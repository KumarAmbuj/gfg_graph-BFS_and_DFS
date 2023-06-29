from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)


    def dfs(self,u,vis,color,x):

        color[1-x]+=1
        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis,color,1-x)

    def bipartite(self):

        vis=[False for i in range(self.v)]

        color=[0,0]

        self.dfs(0,vis,color,0)

        print(color[0]*color[1]-(self.v-1))

n = 5
g=Graph(n)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,4)
g.bipartite()

