n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
groupCnt = min(n , m) // 2
for _ in range(0, r):
    for i in range(groupCnt):
        x = i
        y = i
        curValue = arr[x][y]
        #좌
        for j in range(i + 1, n - i):
            x = j
            preValue = arr[x][y]
            arr[x][y] = curValue
            curValue = preValue
        for j in range(i + 1, m - i):
            y = j
            preValue = arr[x][y]
            arr[x][y] = curValue
            curValue = preValue
        for j in range(n - 2 - i, i - 1, -1):
            x = j
            preValue = arr[x][y]
            arr[x][y] = curValue
            curValue = preValue
        for j in range(m - 2 - i, i - 1, -1):
            y = j
            preValue = arr[x][y]
            arr[x][y] = curValue
            curValue = preValue

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()
