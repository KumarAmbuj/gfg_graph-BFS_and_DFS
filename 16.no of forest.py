from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis):

        vis[u]=True

        for v in self.graph[u]:
            if vis[v]==False:
                self.dfs(v,vis)

    def treesno(self):

        count=0
        vis=[False for j in range(self.v)]
        for i in range(self.v):
            if vis[i]==False:
                self.dfs(i,vis)
                count+=1
        print(count)


V = 5
g=Graph(V)
g.addEdge( 0, 1)
g.addEdge( 0, 2)
g.addEdge( 3, 4)
g.treesno()