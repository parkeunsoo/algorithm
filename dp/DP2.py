
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else :
        return f(n-1)+f(n-2)+f(n-3)

T = int(input())
c = list()
for _ in range(T):
    n = int(input())
    c.append(f(n))
for i in range(T):
    print(c[i])

