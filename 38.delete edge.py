from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,u,mn,vis,sm,arr):

        vis[u]=True
        x=0
        z=0
        for v in self.graph[u]:
            if vis[v]==False:
                x = self.dfs(v, mn, vis, sm, arr)
                mn[0]=min(mn[0],sm-2*x)
                z=z+x


        return z+arr[u]


    def findmindiff(self,e,arr):

        for x in e:
            self.addEdge(x[0],x[1])

        sm=sum(arr)

        vis=[False for i in range(len(arr))]

        mn=[9999]

        x=self.dfs(0,mn,vis,sm,arr)
        print(mn[0])


vertex = [4, 2, 1, 6, 3, 5, 2]
edges = [[0, 1], [0, 2], [0, 3],
            [2, 4], [2, 5], [3, 6]]
N = len(vertex)
g=Graph(N)
g.findmindiff(edges,vertex)