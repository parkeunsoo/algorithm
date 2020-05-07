import sys 

N = int(sys.stdin.readline())
answer = list()
for _ in range(N):
    M = int(sys.stdin.readline())
    dp = list([1]*M)
    for i in range(3,M):
        dp[i] = dp[i-2] + dp[i-3]
    answer.append(dp[M-1])

for i in range(N):
    print(answer[i])
