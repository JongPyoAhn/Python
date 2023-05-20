'''
n개의 바구니에 사과가 있을수도 있고 없을 수도 있다.
사과먹는 벌레를 특정 위치에 두고 싶다.
자기와 가장 가까운 위치에서부터 사과를 먹기 시작
1 2 3 4 5 |바구니 번호 
0 1 0 1 0 |사과 유무
벌레가 3번에 떨어지면? 같은 거리에 있는 사과가 2개 있으므로 오류를 일으키고 죽는다.
벌레가 모든 사과를 먹을 수 있는 시작점 중에서 x와 가장 가까운 거리
n <= 300
1 <= x <= n
'''
n, x = map(int, input().split())
nArr = list(map(int, input().split()))
answer = n + 1
x -= 1
for start in range(n):
    cur = start
    for i in range(n):
        if nArr[i] == 2:
            nArr[i] = 1
    while True:
        #1. 가장 가까운 사과까지의 거리 계산
        min_dist = n + 1
        for i in range(n):
            if nArr[i] == 1:
                min_dist = min(min_dist, abs(i - cur))
        #2. 현재 사과를 다먹었다면 멈춘다.
        if min_dist == n + 1:
            answer = min(answer, abs(start - x))
            break
        
        #3. 같은 거리에 사과가 두개 있는지 확인
        left = cur - min_dist 
        right = cur + min_dist
        if left >= 0 and nArr[left] == 1 and right < n and nArr[right] == 1:
            break
        
        #4. 사과를 먹은거 체크
        if 0 <= left and nArr[left] == 1:
            cur = left
            nArr[left] = 2
        else:
            cur = right
            nArr[right] = 2
print(answer)        


        
'''
17 9
1 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1
=>
3
'''