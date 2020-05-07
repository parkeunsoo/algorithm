import sys
N = int(sys.stdin.readline())
v = list(map(int,sys.stdin.readline().split()))
a = list([0]*N)
b = list([0])
sol = list()
for value in v:
    if a[value-1] ==  0:
        a[value-1] = 1 
    if max(b) + 1 > a[value-1]:
        a[value-1] = max(a) + 1
    b.append(a[value-1])
print(b)
print(a)
print(max(a))