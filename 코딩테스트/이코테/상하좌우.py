#맞
import sys
si = sys.stdin.readline
n = int(si())
orders = list(si().split())
cur = [1, 1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]
for order in orders:
    for i in range(len(move_types)):
        if order == move_types[i]:
            cur[0] += dx[i]
            cur[1] += dy[i]
            if cur[0] < 1 or cur[0] > n or cur[1] < 1 or cur[1] > n:
                cur[0] -= dx[i]
                cur[1] -= dy[i]
                
print(f'{cur[0]} {cur[1]}')