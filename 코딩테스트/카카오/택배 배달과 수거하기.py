def solution(cap, n, deliveries, pickups):
    deliveries = deliveries
    pickups = pickups
    
    i, j = n - 1, n - 1
    
    while i >= 0 and deliveries[i] == 0:
        i -= 1
    
    while j >= 0 and pickups[j] == 0:
        j -= 1
        
    answer = 0
    while i >= 0 or j >= 0:
        cur = cap
        answer += (max(i, j) + 1) * 2
        
        while i >= 0 and cur:
            if deliveries[i] > cur:
                deliveries[i] -= cur
                cur = 0
            else:
                cur -= deliveries[i]
                deliveries[i] = 0
                while i >= 0 and deliveries[i] == 0:
                    i -= 1
        cur = cap
        while j >= 0 and cur:
            if pickups[j] > cur:
                pickups[j] -= cur
                cur = 0
            else:
                cur -= pickups[j]
                pickups[j] = 0
                while j >= 0 and pickups[j] == 0:
                    j -= 1
                    
    return answer