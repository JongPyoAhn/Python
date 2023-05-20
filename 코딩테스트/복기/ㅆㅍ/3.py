'''
바구니가 1~5000번까지 존재한다.
이 중에서 n개의 바구니에만 사과가 들어있다.
11번부터는 다 사과가 없고 1번, 3번, 4번, 6번, 8번, 10번에 있다면
1 2 3 4 5 6 7 8 9 10|바구니번호
1 0 1 1 0 1 0 0 1 1|사과존재여부
벌레의 시작위치는 S이다.
S에서 벌레가 출발해서 모든 사과를 다 먹는데 필요한 최단시간
벌레가 4번에서 시작을 하면, 왼쪽과 오른쪽으로 내맘대로 움직일 수 있는데,
모든사과를 먹기위해서 벌레가 이동해야하는 총 이동 횟수의 최솟값을 구하라.
n <= 300
'''

n, s = map(int, input().split())
nArr = list(map(int, input().split()))
answer = 0
s -= 1
def leftSolve(start):
    cur = start
    result = 0
    if nArr[cur] == 1: #현재위치가 사과인경우
        nArr[cur] = 2
    #왼쪽 먼저 탐색
    while True:
        move = 0 # 이동횟수
        if cur > 0:#왼쪽에 원소가 있는 경우
            # 탐색하면서 1이 없으면 가지말고 1을 발견하면 이동횟수 추가하고 2로 변경
            for i in range(cur, -1, -1):
                if nArr[i] == 1:#사과가 있으면 탐색해야된다.
                    move = abs(i - cur) # 이동횟수 추가
                    cur = i #이동
                    result += move
                    nArr[i] = 2
        if move == 0: #왼쪽에 이동할 곳이 더이상 없으므로 멈춘다.
            break
    #오른쪽 탐색
    while True:
        move = 0 # 이동횟수
        if cur < n:# 현재위치가 오른쪽 끝이 아니면
            # 탐색하면서 1이 없으면 가지말고 1을 발견하면 이동횟수 추가하고 2로 변경
            for i in range(cur, n):
                if nArr[i] == 1:#사과가 있으면 탐색해야된다.
                    move = abs(i - cur) # 이동횟수 추가
                    cur = i #이동
                    result += move
                    nArr[i] = 2
        if move == 0: #오른쪽에 이동할 곳이 더이상 없으므로 멈춘다.
            break            
    return result
        
def rightSolve(start):
    for i in range(n):
        if nArr[i] == 2:
            nArr[i] = 1
    cur = start
    result = 0
    if nArr[cur] == 1: #현재위치가 사과인경우
        nArr[cur] = 2
    #오른쪽 탐색
    while True:
        move = 0 # 이동횟수
        if cur < n:# 현재위치가 오른쪽 끝이 아니면
            # 탐색하면서 1이 없으면 가지말고 1을 발견하면 이동횟수 추가하고 2로 변경
            for i in range(cur, n):
                if nArr[i] == 1:#사과가 있으면 탐색해야된다.
                    move = abs(i - cur) # 이동횟수 추가
                    cur = i #이동
                    result += move
                    nArr[i] = 2
        if move == 0: #오른쪽에 이동할 곳이 더이상 없으므로 멈춘다.
            break  
    #왼쪽 먼저 탐색
    while True:
        move = 0 # 이동횟수
        if cur > 0:# 왼쪽에 원소가 있는 경우
            # 탐색하면서 1이 없으면 가지말고 1을 발견하면 이동횟수 추가하고 2로 변경
            for i in range(cur, -1, -1):
                if nArr[i] == 1:#사과가 있으면 탐색해야된다.
                    move = abs(i - cur) # 이동횟수 추가
                    cur = i #이동
                    result += move
                    nArr[i] = 2
        if move == 0: #왼쪽에 이동할 곳이 더이상 없으므로 멈춘다.
            break
        
    return result
        
    
answer = min(leftSolve(s), rightSolve(s))
print(answer)
    
            
'''
10 4
1 0 1 1 0 1 0 0 1 1
=>
12
'''         
                    
        
            
            