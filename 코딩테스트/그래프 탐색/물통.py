from collections import deque
answer = set([])
def bfs(a, b, c):
    queue = deque([(0, 0, c)])
    visited = [[[False for _ in range(201)]for _ in range(201)] for _ in range(201)]
    visited[0][0][c] = True
    
    while queue:
        curA, curB, curC = queue.popleft()
        if curA == 0:
            answer.add(curC)
        #a에서 b와 c로 분배
        if curA != 0:
            diff = b - curB
            if curA >= diff and not visited[curA - diff][curB + diff][curC]:
                queue.append((curA - diff, curB + diff, curC))
                visited[curA - diff][curB + diff][curC] = True
            if curA < diff and not visited[0][curB + curA][curC]:
                queue.append((0, curB + curA, curC))
                visited[0][curB + curA][curC] = True
            
            diff = c - curC
            if curA >= diff and not visited[curA - diff][curB][curC + diff]:
                queue.append((curA - diff, curB, curC + diff))
                visited[curA - diff][curB][curC + diff] = True
            if curA < diff and not visited[0][curB][curC + curA]:
                queue.append((0, curB, curC + curA))
                visited[0][curB][curC + curA] = True
                
        #b에서 a와 c로 분배
        if curB != 0:
            diff = a - curA
            if curB >= diff and not visited[curA + diff][curB - diff][curC]:
                queue.append((curA + diff, curB - diff, curC))
                visited[curA + diff][curB - diff][curC] = True
            if curB < diff and not visited[curA + curB][0][curC]:
                queue.append((curA + curB, 0, curC))
                visited[curA + curB][0][curC] = True
                
            diff = c - curC
            if curB >= diff and not visited[curA][curB - diff][curC + diff]:
                queue.append((curA, curB - diff, curC + diff))
                visited[curA][curB - diff][curC + diff] = True
            if curB < diff and not visited[curA][0][curC + curB]:
                queue.append((curA, 0, curC + curB))
                visited[curA][0][curC + curB] = True    
        
        #c에서 a와 b로 분배
        if curC != 0:
            diff = a - curA
            if curC >= diff and not visited[curA + diff][curB][curC - diff]:
                queue.append((curA + diff, curB, curC - diff))
                visited[curA + diff][curB][curC - diff] = True
            if curC < diff and not visited[curA + curC][curB][0]:
                queue.append((curA + curC, curB, 0))
                visited[curA + curC][curB][0] = True
            
            diff = b - curB
            if curC >= diff and not visited[curA][curB + diff][curC - diff]:
                queue.append((curA, curB + diff, curC - diff))
                visited[curA][curB + diff][curC - diff] = True
            if curC < diff and not visited[curA][curB + curC][0]:
                queue.append((curA, curB + curC, 0))
                visited[curA][curB + curC][0] = True
a, b, c = map(int, input().split())
bfs(a, b, c)

listed = list(answer)
listed.sort()

print(" ".join(list(map(str, listed))))