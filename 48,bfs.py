class Pair:
    def __init__(self,u,psf):
        self.u=u
        self.psf=psf

def Queue():
    queue=[]
    return queue
def Enqueue(queue,x):
    queue.append(x)
def Dequeue(queue):
    return queue.pop(0)
def Size(queue):
    return len(queue)

from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def sameside(self,n1,n2):
        n1=str(n1)
        n2=str(n2)
        queue=Queue()
        vis=[False for i in range(self.v)]
        Enqueue(queue,Pair(1,str(1)))
        while(Size(queue)):

            rem=Dequeue(queue)

            if vis[rem.u-1]==True:
                continue

            vis[rem.u-1]=True

            if n1 in rem.psf and n2 in rem.psf:
                return True

            for v in self.graph[rem.u]:
                if vis[v-1]==False:
                    Enqueue(queue,Pair(v,rem.psf+str(v)))

        return False

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

print(g.sameside(1,5))
print(g.sameside(2,9))
print(g.sameside(2,6))


