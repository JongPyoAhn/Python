n, m = map(int, input().split(" "))
arr = [[]]
for i in range(0, n):
    a = list(map(int, input().split(" ")))
    arr.append(a)
arr.pop(0)
result = 0

for i in range(0, n):
    temp = min(arr[i])
    result = max(temp, result)
        
print(result)