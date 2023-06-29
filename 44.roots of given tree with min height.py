from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,vis):
        mx=0
        vis[u]=True
        for v in self.graph[u]:
            if vis[v]==False:
                mx=max(mx,1+self.dfs(v,vis))
        return mx

    def findminheight(self):
        root=-1
        height=999

        for i in range(self.v):
            vis=[False for i in range(self.v)]
            h=self.dfs(i,vis)
            
            if h<height:
                height=h
                root=i

        print(root,height)

g = Graph(6,)
g.addEdge(0, 3)
g.addEdge(1, 3)
g.addEdge(2, 3)
g.addEdge(4, 3)
g.addEdge(5, 4)
g.findminheight()