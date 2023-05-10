import sys
from collections import deque
si = sys.stdin.readline
r, c = map(int, si().split())
forest = [list(map(str, si().strip('\n'))) for _ in range(r)]

cave = (0, 0)
hedgehog = (0, 0)
waters = []

for i in range(r):
    for j in range(c):
        if forest[i][j] == "D":
            cave = (i, j)
        if forest[i][j] == "S":
            hedgehog = (i, j)
        if forest[i][j] == "*":
            waters.append((i, j))


dx = [-1 , 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    deq = deque()
    visited = [[False for _ in range(c)] for _ in range(r)]
    
    for water in waters:
        deq.append((water[0], water[1], 0, 0))
        visited[water[0]][water[1]] = True
    
    deq.append((hedgehog[0], hedgehog[1], 0, 1))# x, y, time, 물 = 0 호그 = 1
    visited[hedgehog[0]][hedgehog[1]] = True
    
    while deq:
        curX, curY, curTime, what = deq.popleft()
        if curX == cave[0] and curY == cave[1]:
            return curTime
        for i in range(4):
            nx = curX + dx[i]
            ny = curY + dy[i]
            
            if nx < 0 or ny < 0 or nx >= r or ny >= c: continue
            if what == 0 and (nx, ny) == cave: continue
            if forest[nx][ny] == 'X': continue
            if visited[nx][ny]: continue
            deq.append((nx, ny, curTime + 1, what))
            visited[nx][ny] = True
            
    return 0

answer = bfs()
if answer == 0:
    print("KAKTUS")
else:
    print(answer)
    