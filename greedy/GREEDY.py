import sys
N = int(input())
meeting = list()
for _ in range(N):
    meeting.append(list(map(int,sys.stdin.readline().split())))
meeting = sorted(meeting, key=lambda end : [end[1],end[0]])

def batch():
    end = 0
    count = 0
    for meet in meeting:
        if meet[0] >= end:
            end = meet[1]
            count +=1
    return count
    
print(batch())