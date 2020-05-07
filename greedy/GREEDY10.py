import sys
import itertools
number = ['0','1','2','3','4','5','6','7','8','9']

N = int(sys.stdin.readline())
ine = list(sys.stdin.readline().split())
pem = list(map(''.join,itertools.permutations(number,N+1)))

def minn(pem):
    sol = 0
    for j in range(len(pem)):
        for i in range(N):
            if ine[i] == '<':
                if pem[j][i] > pem[j][i+1]:
                    sol = 1
                    break
            elif ine[i] == '>':
                if pem[j][i] < pem[j][i+1]:
                    sol = 1
                    break
        if sol == 0:
            return pem[j]
        sol = 0

def maxn(pem):
    sol = 0
    for j in range(len(pem)):
        for i in range(N):
            if ine[i] == '<':
                if pem[j][i] > pem[j][i+1]:
                    sol = 1
                    break
            elif ine[i] == '>':
                if pem[j][i] < pem[j][i+1]:
                    sol = 1 
                    break
        if sol == 0:
            return pem[j]
        sol = 0

pem.sort(reverse=True)
print(maxn(pem))
pem.sort()
print(minn(pem))

