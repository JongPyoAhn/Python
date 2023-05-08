import sys
si = sys.stdin.readline
n = int(si())
arr = list(map(int, si().split()))
m = int(si())
answer = 0
sum = 0
maxArr = max(arr)
for i in arr:
    sum += i
    
    
def determine(x: int) -> bool:
    deterSum = 0
    for i in arr:
        deterSum += min(x, i)
    if deterSum <= m: #가능한 경우
        return True
    else:
        return False
        


if sum <= m:
    answer = maxArr
else:
    s = 1
    e = maxArr
    while s <= e:
        mid = (s + e) // 2
        if determine(mid):
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
print(answer)