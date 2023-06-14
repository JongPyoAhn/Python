import sys
si = sys.stdin.readline
n, m = map(int, si().split())
x, y, d = map(int, si().split())
arr = [list(map(int, si().split())) for i in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 0 #네방향 모두 가본칸인지 확인
answer = 1
arr[x][y] = 2
while True:
    cnt += 1
    d -= 1
    if d == -1:
        d = 3
    #왼쪽방향에 가보지않은 칸 존재하는지 체크
    nx = x
    ny = y
    while True:
        nx += dx[d]
        ny += dy[d]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:#범위를 넘어간다면
            break
        if arr[nx][ny] == 0: #가보지 않은칸이 존재한다면
            #왼쪽방향으로 회전해서 한칸 전진
            x += dx[d]
            y += dy[d]
            if arr[x][y] == 0: #전진한 칸이 가보지않은 칸이면 체크
                arr[x][y] = 2
                answer += 1
            cnt = 0
            break
    if cnt == 4: #네방향모두 가본칸인거나 바다로 되어있는 칸인경우
        x -= dx[d]
        y -= dy[d]
        cnt = 0
        if arr[x][y] == 1:#바다인경우 멈춘다.
            break
print(answer)
        
'''
4 4
1 1 0
1 1 1 1
1 0 0 1
1 1 0 1
1 1 1 1
'''
