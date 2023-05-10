'''
수의 위치가 다르면 값이 같아도 다른 수(수열 의미하는것같다)
# 다른 수 두개의 합 (좋다)
# 찾은 반례
# 11   
# 0 1 2 3 4 5 6 7 8 9 10 
# 이건 어떤 수가 만들어지기 위해 "다른" 두수를 써야하면 2를 만들 수 없는데,
if i == s: s += 1
elif i == e: e -= 1
이게 없으면 다른 두수가 아닌 "어떤수"까지 포함할 수 있어서 틀렸었던것이다.
'''
import sys
si = sys.stdin.readline
n = int(si())
nArr = list(map(int, si().split()))
nArr.sort()

count = 0
sum = 0
answer = []

for i in range(n):
    s = 0
    e = n - 1
    while s < e:
        if i == s: s += 1
        elif i == e: e -= 1
        else:
            if nArr[s] + nArr[e] < nArr[i]:
                s += 1
            elif nArr[s] + nArr[e] > nArr[i]:
                e -= 1
            else:
                answer.append(nArr[i])
                break        
print(len(answer))