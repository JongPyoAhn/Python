import sys
si = sys.stdin.readline
n, m = map(int, si().split())
arr = list(map(int, si().split()))

def determine(x: int) -> bool:
    sum = 0
    bluelay = []
    for i in arr:
        if sum + i > x:
            bluelay.append(sum)
            sum = i
        else:
            sum += i
    bluelay.append(sum)
    
    if len(bluelay) < m:
        return False
    elif len(bluelay) > m:
        return True
    
    if max(bluelay) <= x:
        return False
    else:
        return True
    

s = 1
e = 1000000000
answer = 0
while s <= e:
    mid = (s + e) // 2
    if determine(mid):
        s = mid + 1
    else:
        answer = mid
        e = mid - 1
print(answer)