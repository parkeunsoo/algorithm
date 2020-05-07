import sys
N = int(sys.stdin.readline())
answer = list()
for _ in range(N):
    sol = list()
    M = int(sys.stdin.readline())
    queue = list([0] for _ in range(M+1))
    for i in range(1,M+1):
        x,y = map(int,sys.stdin.readline().split())
        queue[x] = y
    ans = M+1
    for i in range(1,M+1):
            if queue[i] < ans:
                sol.append(i)
                ans = queue[i]
    answer.append(len(sol))
for i in range(N):
    print(answer[i])
