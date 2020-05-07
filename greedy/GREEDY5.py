import sys
N, M, K = map(int,sys.stdin.readline().split())

def sol(N,M,K):
    while K:
        if N>2*M:
            N -= 1
        else:
            M -= 1
        K -= 1      
    return min(N//2,M)

print(sol(N,M,K))
    
