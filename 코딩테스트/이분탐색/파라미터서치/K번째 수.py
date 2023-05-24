import sys
si = sys.stdin.readline
n = int(si())
k = int(si())

def determine(target):
    #target보다 작은 수가 K개가 되는지 안되는지(결정문제)
    sum = 0
    for i in range(1, n + 1):
        sum += min(n, target // i)
    return sum >= k

s, e, answer = 1, 10000000000, 0
while s <= e:
    mid = (s + e) // 2
    if determine(mid):
        e = mid - 1
        answer = mid
    else:
        s = mid + 1
        
print(answer)