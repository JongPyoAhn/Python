import heapq
import sys
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s].append((e, cost))
    
start, end = map(int, input().split())
def dijkstra(n, graph, start, end):
    pq = []
    dist = [sys.maxsize for i in range(n + 1)]
    heapq.heappush(pq, (start, 0))
    
    while pq:
        curNode, curCost = heapq.heappop(pq)
        
        if dist[curNode] < curCost:
            continue
        
        for i in range(len(graph[curNode])):
            nextNode = graph[curNode][i][0]
            nextCost = graph[curNode][i][1]
            
            if dist[nextNode] > nextCost + curCost:
                heapq.heappush(pq, (nextNode, nextCost + curCost))
                dist[nextNode] = nextCost + curCost

    return dist[end]

print(dijkstra(n, graph, start, end))