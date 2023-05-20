'''
길이가 n인 수열 (음수가 있을 수 있고 양수가 있을 수 있다.)
i = 1, 2, 3, 4
A[i] = [-1, 1, -2, 3]
n개의 원소의 합이 2 * n 이상이 되게 하고 싶어요.
- 1 + 1 - 2 + 3 = 1
내 목표는 2 * 4 니까 8 이상을 가져와야하는데,
나는 마법을 부릴 수 있다.
각 인덱스마다 최대 1번 적용 가능하다.
마법을 i번인덱스에 쓰면 if A[i] == 이미 양수? A[i] + i : i
만약 A[4]에 마법을 부리면 7로 바뀜
만약 A[3]에 마법을 부리면 인덱스 값인 3으로 바뀜
모든위치에 마법을 쓰면 조건을 만족한다.
하지만, 최소한의 횟수의 마법을 쓰고 싶다.
4 <= n <= 1,000
|A[i]| <= 100,000
'''
arr = list(map(int, input().split()))
dp = []
n = len(arr)
for i in range(n):
    if arr[i] >= 0:
        arr[i] = arr[i] + i
    else:
        arr[i] = i

arr.sort()
answer = 0
result = 0
for i in range(n - 1, -1, -1):
    result += arr[i]
    answer += 1
    if result >= 2 * n:
        break
print(answer)


# i = 마법을 쓰는 횟수 dp[i] = 최댓값
# arr[1] = 1
# dp[i] = max()
        
