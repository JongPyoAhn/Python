# 0 ~ n
# 가로등을 설치할 개수 M
# 가로등의 위치 x
# 굴다리 모든 길을 밝힐 수 있는(결정문제) 가로등의 최소한 높이(파라미터)
import sys
si = sys.stdin.readline

n = int(si())
m = int(si())
lampList = list(map(int, si().split()))

#O(n)
def determine(lampHeight):
    #lampHeight으로 굴다리 모든 길을 밝힐 수 있는가?
    last = 0
    for x in lampList:
        if x - last <= lampHeight:
            last = x + lampHeight
        else:
            return False
    return last >= n
        
s, e, answer = 1, n + 1, 0
#O(n log n)
while s <= e:
    mid = (s + e) // 2
    if determine(mid):
        e = mid - 1
        answer = mid
    else:
        s = mid + 1
print(answer)