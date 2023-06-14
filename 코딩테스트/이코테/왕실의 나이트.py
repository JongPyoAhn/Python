import sys
si = sys.stdin.readline
readLoc = list(map(str, si().strip()))
dx = [1, 1, -1, -1, -2, 2, -2, 2]
dy = [-2, 2, -2, 2, 1, 1, -1, -1]
cur = [int(readLoc[1]), 0]
if readLoc[0] == 'a':
    cur[1] = 1
elif readLoc[0] == 'b':
    cur[1] = 2
elif readLoc[0] == 'c':
    cur[1] = 3
elif readLoc[0] == 'd':
    cur[1] = 4
elif readLoc[0] == 'e':
    cur[1] = 5
elif readLoc[0] == 'f':
    cur[1] = 6
elif readLoc[0] == 'g':
    cur[1] = 7
elif readLoc[0] == 'h':
    cur[1] = 8
answer = 0
for i in range(8):
    nx = cur[0] + dx[i]
    ny = cur[1] + dy[i]
    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    answer += 1
    
print(answer)

    
