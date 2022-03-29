
n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
groupCnt = min(n, m) // 2
raw = n
col = m

def rotate(i):
    length = (raw - 1) * 2 + (col - 1) * 2
    row = [0] * length
    idx = 0

    for y in range(i, m - i):
        row[(idx - r) % length] = arr[i][y]
        idx += 1  
    for x in range(i + 1, n - i):
        row[(idx - r) % length] = arr[x][m - i - 1]
        idx += 1
    for y in range(m - i - 2, i - 1, -1):
        row[(idx - r) % length] = arr[n - i - 1][y]
        idx += 1
    for x in range(n - i - 2, i - 1, -1):
        row[(idx - r) % length] = arr[x][i]
        idx += 1
    
    idx = 0
    for y in range(i, m - i):
        arr[i][y] = row[idx]
        idx += 1

    for x in range(i + 1, n - i):
        arr[x][m - i - 1] = row[idx]
        idx += 1
        
    for y in range(m - i - 2, i - 1, -1):        
        arr[n - i - 1][y] = row[idx]
        idx += 1
    for x in range(n - i - 2, i, -1):
        arr[x][i] = row[idx]
        idx += 1

def solve():
    global raw, col
    for i in range(groupCnt):
        rotate(i)
        raw -= 2
        col -= 2

solve()
for i in arr:
    print(*i)