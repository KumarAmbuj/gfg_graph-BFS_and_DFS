from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def dfs(self,u,vis,psf,n1,n2):


        vis[u-1] = True
        if n1 in psf and n2 in psf:
            return True




        for v in self.graph[u]:
            if vis[v-1]==False:
                if self.dfs(v,vis,psf+str(v),n1,n2):
                    return True
        return False


    def sameside(self,n1,n2):

        vis=[False for i in range(self.v)]
        print(self.dfs(1,vis,str(1),str(n1),str(n2)))

n = 9
g=Graph(n)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,6)
g.addEdge(2,4)
g.addEdge(2,5)
g.addEdge(5,7)
g.addEdge(5,8)
g.addEdge(5,9)

g.sameside(1,5)
g.sameside(2,9)
g.sameside(2,6)
