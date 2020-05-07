import sys
cost = int(sys.stdin.readline())
change = 1000 - cost

def JOI(change):
    coin = [1000,500,100,50,10,5,1]
    count = 0
    for coin in coin:
        count += change//coin
        change = change%coin
        if change == 0:
            break
    return count
print(JOI(change))