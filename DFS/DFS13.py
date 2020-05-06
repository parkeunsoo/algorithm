#9466
import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
count = list([0]*T)

def dfs(s):
    if visit[s] == True:
        if s in check:
            index = check.index(s)
            return index
        else :
            return None 
    check.append(s)
    visit[s] = True
    v = dfs(value[s])
    return v
    
for j in range(T):
    count[j] = 0
    cou = 0
    n = int(sys.stdin.readline())
    value = [0] + list(map(int,sys.stdin.readline().split()))
    visit = list([False]*(n+1))
    a = []
    for i in range(1,n+1):
        check = list()
        if visit[i] == False:
            result = dfs(i)
            if result != None:
                a += check[result:]
    count[j] = n - len(a)
for i in range(T):
    print(count[i])