N = int(input())
r = [False]*(N+1)
def f(N):
    for i in range(1,N+1):
        if i==0 or i==1:
            r[i]=0  
        else:
            r[i] = r[i-1]+1
            if i%3==0:
                if r[i] > r[i//3]+1:
                    r[i] = r[i//3]+1
            if i%2==0:
                if r[i] > r[i//2]+1:
                    r[i] = r[i//2]+1
    return r[N]
print(f(N))
