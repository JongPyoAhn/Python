#set을 이용한 풀이
# n, m = map(int, input().split())
# nSet = {input() for i in range(n)}
# mSet = {input() for i in range(m)}
# inter = list(nSet.intersection(mSet))
# inter.sort()

# print(len(inter))
# [print(i) for i in inter]

#이분탐색을 이용한 풀이
n, m = map(int, input().split())
nArr = list([input() for i in range(n)])
mArr = list([input() for i in range(m)])

mArr.sort()
answer = []
for x in nArr:
    s = 0
    e = m - 1
    while s <= e:
        mid = (s + e) // 2
        if mArr[mid] < x:
            s = mid + 1
        elif mArr[mid] > x:
            e = mid - 1
        else:
            answer.append(x)
            break
print(len(answer))
answer.sort()
[print(i) for i in answer]