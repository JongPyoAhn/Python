#O
import sys
from collections import deque
si = sys.stdin.readline
computerCount = int(si())
lineCount = int(si())
graph = [[] for i in range(computerCount + 1)]
que = deque()
for _ in range(lineCount):
    read = list(map(int, si().split()))
    graph[read[0]].append(read[1])
    graph[read[1]].append(read[0])
answer = -1
def bfs():
    global answer
    visited = [False for i in range(computerCount + 1)]
    que.append(1)
    while que:
        popped = que.popleft()
        if not visited[popped]:        
            visited[popped] = True
            answer += 1
            for col in graph[popped]:
                que.append(col)
bfs()
print(answer)
            