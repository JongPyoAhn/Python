n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
inst = list(map(int, input().split()))
#가장처음 주사위 모든면에 0이 적혀있다.
#이동한 칸의 수가 0이면, 주사위 바닥면에 쓰여있는 수가 칸에 복사된다.
#0이 아닌 경우에는 칸에 쓰여있는 수가 주사이의 바닥으로 복사되고 칸은 0이된다.
dice = [[0] * 3 for _ in range(4)]

#지금 고려해야할것
#주사위 회전
#남쪽으로 이동시 주사위 위에서 아래로 밀리게하면됨.
#북쪽으로 이동시 주사위 아래에서 위로 밀리게
#동쪽에서 서쪽으로 이동시 가로방향 왼쪾에서 오른쪽으로 밀리게
#서쪽에서 동쪽으로 이동시 가로방향 오른쪾에서 왼쪽으로 밀리게

#무조건 [3][1]이 바닥임.
for i in inst:
    if i == 4:
        if x + 1 >= n:
            continue
        x += 1
        cur = dice[0][1]
        for j in range(1, 4):
            temp = dice[j][1]
            dice[j][1] = cur
            cur = temp
        dice[0][1] = cur
        
    if i == 3:
        if x - 1 < 0:
            continue
        cur = dice[3][1]
        for j in range(2, -1, -1):
            temp = dice[j][1]
            dice[j][1] = cur
            cur = temp
        dice[3][1] = cur
        x -= 1
    if i == 2:
        if y - 1 < 0:
            continue
        y -= 1
        cur = dice[3][1]
        for j in range(2, -1, -1):
            temp = dice[1][j]
            dice[1][j] = cur
            cur = temp
        dice[3][1] = cur
        
    if i == 1:
        if y + 1 >=m:
            continue
        y += 1
        cur = dice[3][1]
        for j in range(0, 3):
            temp = dice[1][j]
            dice[1][j] = cur
            cur = temp
        dice[3][1] = cur
    if arr[x][y] == 0:
        arr[x][y] = dice[3][1]
    else:
        dice[3][1] = arr[x][y]
        arr[x][y] = 0
    # print(dice)
    print(dice[1][1])
    # print(i)
    # print(dice)
