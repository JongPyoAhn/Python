n = int(input())
nArr = list(map(int, input().split()))
nArr.sort()
answer = []
compare = 2000000000

for x in nArr:
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        if nArr[mid] + x < 0:
            s = mid + 1
        elif nArr[mid] + x > 0:
            e = mid - 1
        else:
           answer = [x, nArr[mid]]
           answer.sort()
           break
        if x != nArr[mid]:
           if compare > abs(x + nArr[mid]):
               compare = abs(x + nArr[mid])
               answer = [x, nArr[mid]]
               answer.sort()
print(" ".join(list(map(str, answer))))