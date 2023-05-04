import sys
import heapq


    
    
v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
dist = [sys.maxsize for i in range(v + 1)]
graph = [[] for i in range(v + 1)]
for _ in range(e):
    s, e, c = map(int, sys.stdin.readline().split())
    graph[s].append((e, c))
    
def dijkstra(start, graph):
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        curCost, curNode = heapq.heappop(pq)
        
        if dist[curNode] < curCost:
            continue
        
        for i in range(len(graph[curNode])):
            next = graph[curNode][i][0]
            if dist[next] > curCost + graph[curNode][i][1]:
                heapq.heappush(pq, (curCost + graph[curNode][i][1], next))
                dist[next] = curCost + graph[curNode][i][1]

dijkstra(k, graph)
for i in range(1, len(dist)):
    if i == k:
        print(0)
    elif dist[i] == sys.maxsize:
        print('INF')
    else:
        print(dist[i])
    