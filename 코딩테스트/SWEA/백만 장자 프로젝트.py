# 다시
t = int(input())
for test_case in range(t):
    n = int(input())
    nArr = list(map(int, input().split()))
    answer = 0
    max_price = nArr[n - 1]
    for i in range(n - 1, -1, -1):
        if nArr[i] > max_price:
            max_price = nArr[i]
        else:
            answer += max_price - nArr[i]
    print(f'#{test_case + 1} {answer}')