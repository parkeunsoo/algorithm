import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())
answer = list()

def dfs(s):
    if s in visit:
        return s
    visit.append(s)
    i = (stu[s]-1)
    return dfs(i)


for _ in range(T):
    count = 0
    N = int(sys.stdin.readline())
    stu = list(map(int,sys.stdin.readline().split()))
    check = list([0]*(N))
    for i in stu :
        if check[i]==1:
            continue
        visit = list()
        if i == dfs(i):
            for i in visit:
                check[i] = 1
    for i in check:
        count += i
    answer.append(N-count)
for value in answer:
    print(value)
