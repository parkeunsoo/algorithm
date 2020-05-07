import sys
N = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
prior = list()
value = 0
for i in range(N):
    prior.append(card[i]//i,i)
prior.sort()
