import sys
si = sys.stdin.readline
n = int(si())
arr = [list(map(int, si().split())) for i in range(n)]

def count(A, C, B, X):
    # X이하의 수의 개수 구하는 함수
    if X < A: return 0
    if C < X: return ((C - A) // B) + 1
    return ((X - A) // B) + 1
    
def determine(candidate):
    #하나만 홀수니까 해당 candidate이하의 수가 홀수이면 홀수가 아닐때까지 점점 값을 줄여가면 된다.
    sum = 0
    for i in range(n):
        sum += count(arr[i][0], arr[i][1], arr[i][2], candidate)
    return sum % 2 == 1
target = 0
s, e, answer = 1, 1 << 31, 0
while s <= e:
    mid = (s + e) // 2
    if determine(mid):
        answer = mid
        e = mid - 1
    else:
        s = mid + 1
if answer == 0:
    print('NOTHING')
else:
    cnt = 0
    for i in arr:
        if i[0] <= answer and i[1] >= answer and (answer - i[0]) % i[2] == 0:
           cnt += 1
    print(f'{answer} {cnt}')





