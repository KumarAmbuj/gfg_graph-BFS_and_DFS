def dfs(p,ans,cc):
    ans[p]=1

    for i in range(len(cc[p])):
        if not ans[cc[p][i]]:
            dfs(cc[p][i],ans,cc)

def constructbinarystring(n,k):

    arr=[0 for i in range(n)]
    ans=[0 for i in range(n)]

    for i in range(n):
        arr[i]=i%k

    cc=[[] for i in range(k)]


    for i in range(n//2):
        cc[arr[i]].append(arr[n-1-i])
        cc[arr[n-1-i]].append(arr[i])

    dfs(0,ans,cc)

    for i in range(n):
        print(ans[arr[i]],end='')

    print()

constructbinarystring(7,3)
constructbinarystring(5,3)