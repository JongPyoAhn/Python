# 파라메트릭서치인 이유?
# 1) 막걸리 용량 : 2^31 -1
# 2) 최대키워드
import sys
si = sys.stdin.readline
n, k = map(int, si().split())
arr = [int(input()) for i in range(n)]


def determine(capacity):
    #k명에게 막걸리 분배하는 로직
    cnt = 0
    for x in arr:
        cnt += (x // capacity) #몇명한테 나눠줄 수 있는 지구하기
    return k <= cnt 
    

#구하고자 하는 값 : 최대한 많은양의 막걸리를 분배할 수 있는 용량
#막걸리를 남으면 버린다.
s, e, answer = 0, 1 << 31, 0
while s <= e:
    mid = (s + e) // 2
    if mid == 0:
        answer = 0
        break
    if determine(mid):
        #막걸리가 분배가 된다는 것은 양이 낮다는의미이다.
        s = mid + 1
        answer = mid
    else:
        e = mid - 1
print(1 << 31)
print(1 << 32)
print(1 << 63)
print(answer)