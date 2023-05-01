import heapq
n = int(input())
heap = []
for i in range(n):
    read = list(map(int, input().split()))
    for j in read:
        if len(heap) >= n:
            if heap[0] < j:    
                heapq.heappop(heap)
                heapq.heappush(heap, j)
        else:
            heapq.heappush(heap, j)
        
print(heap[0])