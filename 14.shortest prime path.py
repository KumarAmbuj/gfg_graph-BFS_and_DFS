from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

def findprime(prime):
    lis=[True for i in range(9999+1)]
    n=9999
    p=2
    while(p*p<=n):


        if lis[p]==True:

            for i in range(p*p,n+1,p):
                lis[i]=False
        p+=1

    for i in range(1000,n+1):
        if lis[i]==True:
            prime.append(i)

def isvalid(n1,n2):
    s1=str(n1)
    s2=str(n2)

    c=0

    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            c+=1
    return c==1

def Queue():
    queue=[]
    return queue
def Enqueue(q,x):
    q.append(x)
def Dequeue(q):
    return q.pop(0)
def Size(q):
    return len(q)


def findshortest(s1,s2):
    prime=[]

    findprime(prime)

    g=Graph(10000)

    for i in range(len(prime)-1):
        for j in range(i+1,len(prime)):

            if isvalid(prime[i],prime[j]):
                g.addEdge(prime[i],prime[j])




    l=bfs(s1,s2,prime,g)
    print(l)

def bfs(s1,s2,prime,g):
    vis=[False for i in range(g.v)]

    queue=Queue()
    Enqueue(queue,[s1,0])
    vis[s1]=True

    while(Size(queue)):
        u=Dequeue(queue)

        if u[0]==s2:

            return u[1]

        for v in g.graph[u[0]]:
            if vis[v]==False:
                vis[v]=True
                Enqueue(queue,[v,u[1]+1])
s1=1033
s2=8179
findshortest(s1,s2)



