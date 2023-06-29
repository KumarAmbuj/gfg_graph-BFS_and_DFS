from collections import defaultdict
class Graph:
    def __init__(self):

        self.graph={}

    def addEdge(self,u,v):

        if u not in self.graph:
            self.graph[u]=[]
            self.graph[u].append(v)
        else:
            self.graph[u].append(v)


    def dfs(self,r,u,block):
        mx=0
        ans=[]

        if u==r:

            for v in self.graph[u]:
                if v==block:
                    continue
                z=max(mx,1+self.dfs(r,v,u))
                ans.append(z)
            if len(ans)==1:
                return ans[0]
            elif len(ans)>1:
                mxx = 0
                for i in range(len(ans)-1):
                    for j in range(i+1,len(ans)):
                        mxx=max(mxx,ans[i]+ans[j])
                return mxx

        else:
            for v in self.graph[u]:
                if v ==block:
                    continue
                mx=max(mx,1+ self.dfs(r,v,u))
        return mx



    def findmax(self,e):

        for x in e:
            self.addEdge(x[0],x[1])
            self.addEdge(x[1], x[0])



        mx=0
        for u in self.graph:
            for v in self.graph[u]:

                path1=self.dfs(u,u,v)

                path2=self.dfs(v,v,u)

                mx=max(mx,path1*path2)
        print(mx)

edges = [[1, 8], [2, 6], [3, 1], [5, 3], [7, 8], [8, 4], [8, 6]]
g=Graph()
g.findmax(edges)

edges = [[1, 2], [2, 3], [3, 4]]
g=Graph()
g.findmax(edges)



