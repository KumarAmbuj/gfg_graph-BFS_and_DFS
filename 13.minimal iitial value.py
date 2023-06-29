def issafe(x,y,u,m,n,mat,vis):
    return x>=0 and x<=m and y>=0 and y<=n and (mat[u[0]][u[1]]>=mat[x][y]) and vis[x][y]==False

def dfs(u,vis,m,n,mat):
    vis[u[0]][u[1]]=True
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    for k in range(4):
        x=u[0]+dx[k]
        y=u[1]+dy[k]
        if issafe(x,y,u,m,n,mat,vis):
            dfs([x,y],vis,m,n,mat)


def findminimumvalue(mat,m,n):
    vis=[[False for j in range(n+1)] for i in range(m+1)]

    x=[]
    for i in range(m+1):
        for j in range(n+1):
            x.append(mat[i][j])

    mx=max(x)



    src=[]


    for i in range(m+1):
        for j in range(n+1):
            if mat[i][j]==mx:
                src.append([i,j])


    ans=[]
    flag=False
    for x in src:

        ans.append(x)
        dfs(x,vis,m,n,mat)




        for i in range(m+1):
            for j in range(n+1):
                if vis[i][j]==False:
                    flag=False
                    break
                else:
                    flag=True

            if flag==False:
                break

        if flag:
            break

    for x in ans:
        print(x)


mat=[[1, 2, 3],
        [2, 3, 1],
        [1, 1, 1]]

findminimumvalue(mat,2,2)


mat=[[ 3, 3],

        [1, 1]]

findminimumvalue(mat,1,1)

