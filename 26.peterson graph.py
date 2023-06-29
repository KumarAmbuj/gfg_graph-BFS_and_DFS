adj=[[False for i in range(10)] for j in range(10)]

res=[0]

def findpath(S,v):
    res[0]=v

    for i in range(1,len(S)):

        if adj[v][ord(S[i])-ord('A')]or adj[ord(S[i])-ord('A')][v]:
            v=ord(S[i])-ord('A')
        elif (adj[v][ord(S[i]) - ord('A') + 5] or
                  adj[ord(S[i]) - ord('A') + 5][v]):
            v = ord(S[i]) - ord('A') + 5
        else:
            return False

        res.append(v)
    return True



adj[0][1] = adj[1][2] = adj[2][3] = \
adj[3][4] = adj[4][0] = adj[0][5] = \
adj[1][6] = adj[2][7] = adj[3][8] = \
adj[4][9] = adj[5][7] = adj[7][9] = \
adj[9][6] = adj[6][8] = adj[8][5] = True

S= "ABB"
if findpath(S,ord(S[0])-ord('A')) or findpath(S,ord(S[0])-ord('A')+5):
    print(*res,sep='')
else:
    print(-1)





