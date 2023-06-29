from collections import defaultdict
class Graph:
    def __init__(self,v):
        self.graph=defaultdict(list)
        self.v=v
        self.vdegree=[0 for i in range(self.v)]

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.vdegree[u]+=1
        self.vdegree[v]+=1

    def findcores(self,u,vis,k):
        vis[u]=True




        for v in self.graph[u]:
            if self.vdegree[u] < k:
                self.vdegree[v] -= 1





            if vis[v]==False:
                self.findcores(v, vis, k)
                if self.vdegree[v]<k:
                    self.vdegree[u]-=1





    def findkcores(self,k):

        vis=[False for i in range(self.v)]

        for i in range(self.v):
            if vis[i]==False:
                self.findcores(i, vis, k)


        print(self.vdegree)

        for i in range(self.v):
            if self.vdegree[i]>=k:
                print('[',i,']',end='')
                for v in self.graph[i]:
                    if self.vdegree[v]>=k:
                        print('->',v,end='')
                print()


k = 3;
g1 = Graph (9);
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.findkcores(k)


g2 = Graph(13);
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(0, 3)
g2.addEdge(1, 4)
g2.addEdge(1, 5)
g2.addEdge(1, 6)
g2.addEdge(2, 7)
g2.addEdge(2, 8)
g2.addEdge(2, 9)
g2.addEdge(3, 10)
g2.addEdge(3, 11)
g2.addEdge(3, 12)
g2.findkcores(k)


