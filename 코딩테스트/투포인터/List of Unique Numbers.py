import sys
si = sys.stdin.readline
n = int(si())
nArr = list(map(int, si().split()))
e = -1
ans = 0
dup = set([])
for s in range(n):
    while e + 1 < n and not (nArr[e + 1] in dup):
        dup.add(nArr[e + 1])
        e += 1
    dup.remove(nArr[s])
    ans += e - s + 1
print(ans)
    