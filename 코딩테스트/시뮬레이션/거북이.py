#ok
import sys
si = sys.stdin.readline
t = int(si())
for _ in range(t):
    orders = list(map(str, si().strip()))
    # 북, 동, 남, 서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    curX, curY, d = 0, 0, 0
    xMax, yMax, xMin, yMin = 0, 0, 0, 0
    for order in orders:
        if order == "F": #바라보고 있는 방향으로 전진
            curX += dx[d]
            curY += dy[d]
        elif order == "B": #바라바고 있는 반대 방향으로 전진
            curX -= dx[d]
            curY -= dy[d]
        elif order == "L": #왼쪽방향 90도 회전
            d -= 1
            if d == -1:
                d = 3
        elif order == "R": #오른쪽 방향 90도 회전
            d += 1
            if d == 4:
                d = 0
        xMax = max(xMax, curX)
        yMax = max(yMax, curY)
        xMin = min(xMin, curX)
        yMin = min(yMin, curY)
    if xMax == 0 and xMin == 0:#선분에 있다는 의미
        print(0)
    elif yMax == 0 and yMin == 0:
        print(0)
    else:
        print(f'{(xMax - xMin) * (yMax - yMin)}')
        
        
