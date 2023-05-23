import sys
si = sys.stdin.readline
n, m = map(int, si().split())
arr = [int(si()) for i in range(n)]

def determine(k):
    sum, cnt = 0, 1
    for x in arr:
        if sum + x > k:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt <= m
    

s, e, answer = max(arr), 1000000000, 0
while s <= e:
    mid = (s + e) // 2
    if determine(mid):
        answer = mid
        e = mid - 1
    else:
        s = mid + 1
print(answer)
        

