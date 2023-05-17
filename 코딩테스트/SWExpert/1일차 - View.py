#n <= 1000
for t in range(10):
    n = int(input())
    nArr = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        if i == 0 or i == 1 or i == n - 2 or i == n - 1:
            continue
        cur = nArr[i]
        pre = nArr[i - 1]
        prepre = nArr[i - 2]
        next = nArr[i + 1]
        nextnext = nArr[i + 2]
        result = max(next, nextnext, prepre, pre)
        if cur - result > 0:
            answer += cur - result
        
            
    print(f'#{t + 1} {answer}')
        


