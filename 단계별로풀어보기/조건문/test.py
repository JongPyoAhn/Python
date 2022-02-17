a = int(input())
b = int(input())
c = int(input())
abc = list(map(int, list(str(a * b * c))))
numberCnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(10):
    for j in abc:
        if i == j:
            numberCnt[i] += 1

for i in numberCnt:
    print(i)