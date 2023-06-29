def dfs(curstep,residue,step,wt,arr):
    if curstep>=step:
        return True

    for i in range(len(arr)):
        if arr[i]>residue and arr[i]!=wt[curstep-1]:
            wt[curstep]=arr[i]
            if dfs(curstep+1,arr[i]-residue,step,wt,arr):
                return True
    return False

def findalternating(arr,step):
    wt=[0 for i in range(step)]

    if dfs(0,0,step,wt,arr):
        for i in range(step):
            print(wt[i],end=' ')
    else:
        print('not possible')


arr = [2, 3, 5, 6]
findalternating(arr,10)
print()
arr = [7,11]
findalternating(arr,5)