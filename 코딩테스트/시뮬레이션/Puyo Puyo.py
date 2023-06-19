# 한방컷
import sys
si = sys.stdin.readline
arr = [list(map(str, si())) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def determine(x, y, depth, points):
    visited[x][y] = True
    temp = points
    temp.append((x, y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= 12 or ny >= 6:
            continue
        if not visited[nx][ny] and arr[nx][ny] == arr[x][y]:
            determine(nx, ny, depth + 1, temp)
    return temp
        
answer = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    # 뿌요 아래로 떨어뜨리기
    for j in range(6):
        for i in range(11, -1, -1):#아래에서부터 위로가면서 확인
            if arr[i][j] != ".":#빈칸이 아니라면
                #아래에 있는 좌표를 확인하면서 한칸 씩 내리기
                lastIdx = 0
                for k in range(i, 12):
                    if i == k: continue
                    if arr[k][j] == ".": #빈칸이면
                        #현재 글씨를 한칸 내릴 위치 저장
                        lastIdx = k                        
                    else:#빈칸이 아니면 아래로 내려갈 수 없으므로 바로 멈추기
                        break
                if lastIdx != 0:
                    arr[lastIdx][j] = arr[i][j]
                    #원래 자리는 빈칸으로 채우기
                    arr[i][j] = "."            
    # 같은 색 뿌요가 4개이상 상하좌우 연결된게 존재한다면
    isChain = False
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.':
                continue
            else:
                pointList = determine(i, j, 0, [[]])
                del pointList[0]
                if len(pointList) >= 4: #터진다
                    isChain = True
                    for point in pointList:
                        arr[point[0]][point[1]] = "."#빈칸으로 변경
    if isChain:#체인으로 몇번터졌는지
        answer += 1
    else: #아예 터진 뿌요가 없다면
        break  
    
print(answer)
                    
    
    


'''
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.
'''