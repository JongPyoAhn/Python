import sys
n, m, k = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))

arr.sort(reverse=True)
cnt = 0
sum = 0
for i in range(0, m):
    if cnt == k:
        sum += arr[1]
        cnt = 0
        continue
    sum += arr[0]
    cnt += 1
    


print(sum)
    