t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    nArr = list(map(int, input().split()))
    mArr = list(map(int, input().split()))
    mArr.sort()
    sum = 0
    for i in nArr:
        s = 0
        e = m - 1
        while s <= e:
            mid = (s + e) // 2
            if mArr[mid] < i:
                s = mid + 1
            else:
                e = mid - 1
        sum += s
    print(sum)
                