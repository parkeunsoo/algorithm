import sys
A,B=map(list,sys.stdin.readline().split())
lenA = len(A)
lenB = len(B)
num = lenB - lenA

for _ in range(num):
    A.append(0)
answer = lenB
for _ in range(num+1):
    count = 0
    for i in range(lenB):
        if A[i] != B[i]:
            count += 1
    if count < answer :
        answer = count
    new = A.pop(-1)
    A.insert(0,new)

print(answer-num)