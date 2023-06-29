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

    def findpath(self,s,d):

        vis=[False for i in range(self.v)]
        queue=Queue()
        psf=str(s)

        Enqueue(queue,[s,psf])

        while(Size(queue)):
            rem=Dequeue(queue)

            if rem[0]==d:
                print(rem[1])

            else:
                vis[rem[0]]=True
                for v in self.graph[rem[0]]:
                    if vis[v]==False:
                        Enqueue(queue,[v,rem[1]+str(v)])


v = 4
g=Graph(v)
g.addEdge(0,3)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(2,0)
g.addEdge(2,1)
g.findpath(2,3)



