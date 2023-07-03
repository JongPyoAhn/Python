import sys
import math
si = sys.stdin.readline
n = int(si())
arr = [list(map(int, si().split())) for _ in range(n)]
dir, curState, rotateCnt = -1, 0, 1
dx = [0, 1, 0, -1] #서 남 동 북
dy = [-1, 0, 1, 0]
x, y = n // 2, n // 2 #시작지점
xdx = [[-1, -1, -1, -2, 0, 1, 1, 1, 2, 0], 
       [-1, 0, 1, 0, 2, -1, 0, 1, 0, 1], 
       [-1, -1, -1, -2, 0, 1, 1, 1, 2, 0], 
       [1, 0, -1, 0, -2, 1, 0 , -1, 0, -1]]
ydy = [[1, 0, -1, 0, -2, 1, 0, -1, 0, -1], 
       [-1, -1, -1, -2, 0, 1, 1, 1, 2, 0], 
       [-1, 0, 1, 0, 2, -1, 0, 1, 0, 1], 
       [-1, -1, -1, -2, 0, 1, 1, 1, 2, 0]]
cost = [1, 7, 10, 2, 5, 1, 7, 10, 2]
def direction(dir):
    temp = dir
    temp += 1
    if temp == 4:
        temp = 0
    return temp
answer = 0
while True:
    if curState == 2:
        rotateCnt += 1
        curState = 0
    curState += 1
    dir = direction(dir)
    for i in range(rotateCnt):
        # xx와 yy에 있는 모래를 흩날려야한다.
        xx = x + dx[dir]
        yy = y + dy[dir]
        totalCost = 0
        #흩날리기
        for i in range(9):
            nx = xx + xdx[dir][i]
            ny = yy + ydy[dir][i]
            computedCost = (arr[xx][yy] * cost[i]) // 100
            totalCost += computedCost
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                answer += computedCost
            else:
                arr[nx][ny] += computedCost
        nx = xx + xdx[dir][9]
        ny = yy + ydy[dir][9]
        
        diff = arr[xx][yy] - totalCost
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            answer += diff
        else:
            arr[nx][ny] += diff
        arr[xx][yy] = 0
        x = xx
        y = yy
        if x == 0 and y == 0:
            break
    if x == 0 and y == 0:
        break
    
print(answer)