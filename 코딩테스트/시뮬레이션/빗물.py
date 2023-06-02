import sys
si = sys.stdin.readline
h, w = map(int, si().split())
arr = list(map(int, si().split()))
answer = 0
# for standard in range(w):
#     left, right = 0, 0
#     for i in range(standard, -1, -1):
#         left = max(left, arr[i])
#     for i in range(standard, w):
#         right = max(right, arr[i])
#     if left < right:
#         answer += left - arr[standard]
#     else:
#         answer += right - arr[standard]

for standard in range(1, w - 1):
    left_max = max(arr[:standard])
    right_max = max(arr[standard + 1:])
    compare = min(left_max, right_max)
    if arr[standard] < compare:
        answer += compare - arr[standard]
    
print(answer)