import sys 

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    dp = list([0]*n for _ in range(2))
    p = list([] for _ in range(n))  
    for i in range(2):
        p[i] = list(map(int,sys.stdin.readline().split()))
    for i in range(n):
        dp[0][i] = max(max(dp[1][i-2],dp[0][i-2])+p[0][i], dp[1][i-1]+p[0][i])
        dp[1][i] = max(max(dp[1][i-2],dp[0][i-2])+p[1][i], dp[0][i-1]+p[1][i])
    print(dp)
    print(max(dp[0][n-1],dp[1][n-1]))