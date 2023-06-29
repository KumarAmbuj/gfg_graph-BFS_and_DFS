from collections import defaultdict
def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def findminedge(self,s,d):

        queue=Queue()
        vis=[False for i in range(self.v)]
        Enqueue(queue,[s,str(s)])
        while(Size(queue)):
            rem=Dequeue(queue)

            if rem[0]==d:
                print(len(rem[1])-1)
                break

            else:
                vis[rem[0]]=True

                for v in self.graph[rem[0]]:
                    if vis[v]==False:
                        Enqueue(queue,[v,rem[1]+str(v)])


n = 9
g=Graph(9)
g.addEdge( 0, 1)
g.addEdge( 0, 7)
g.addEdge( 1, 7)
g.addEdge( 1, 2)
g.addEdge( 2, 3)
g.addEdge( 2, 5)
g.addEdge( 2, 8)
g.addEdge(3, 4)
g.addEdge( 3, 5)
g.addEdge( 4, 5)
g.addEdge( 5, 6)
g.addEdge( 6, 7)
g.addEdge( 7, 8)
u = 0
v = 5

g.findminedge(u,v)

