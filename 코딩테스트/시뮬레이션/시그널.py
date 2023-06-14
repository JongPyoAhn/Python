import sys
si = sys.stdin.readline
n = int(si())
a = list(si())
arr = []
tempArr = []
# O(n)
for i in range(n):
    tempArr.append(a[i])    
    if len(tempArr) == n // 5:
        arr.append(tempArr)
        tempArr = []
answer = []
i = 0
while True:
    if i >= n // 5:
        break
    if arr[0][i] == "#":
        # 0
        if not i + 2 >= n //5:
            if arr[1][i] == "#" and arr[1][i + 2] == "#" and arr[2][i + 1] == "." and arr[3][i] == "#" and arr[3][i + 2] == "#" and arr[0][i + 1] == "#":
                answer.append(0)
                i += 3
            # 2
            elif arr[1][i] == "." and arr[1][i + 2] == "#" and arr[2][i + 1] == "#" and arr[3][i] == "#" and arr[3][i + 2] == ".":
                answer.append(2)
                i += 3
            elif arr[1][i] == "." and arr[1][i + 2] == "#" and arr[2][i + 1] == "#" and arr[3][i] == "." and arr[3][i + 2] == "#": 
                answer.append(3)
                i += 3
            elif arr[1][i] == "#" and arr[1][i + 2] == "#" and arr[2][i + 1] == "#" and arr[3][i] == "." and arr[3][i + 2] == "#":
                if arr[0][i + 1] == "#":
                    answer.append(9)
                    i += 3
                else:
                    answer.append(4)
                    i += 3
            elif arr[1][i] == "#" and arr[1][i + 2] == "." and arr[2][i + 1] == "#" and arr[3][i] == "." and arr[3][i + 2] == "#":
                answer.append(5)
                i += 3
            elif arr[1][i] == "#" and arr[1][i + 2] == "." and arr[2][i + 1] == "#" and arr[3][i] == "#" and arr[3][i + 2] == "#":   
                answer.append(6)
                i += 3
            elif arr[1][i] == "." and arr[1][i + 2] == "#" and arr[2][i + 1] == "." and arr[3][i] == "." and arr[3][i + 2] == "#":
                answer.append(7)
                i += 3
            elif arr[1][i] == "#" and arr[1][i + 2] == "#" and arr[2][i + 1] == "#" and arr[3][i] == "#" and arr[3][i + 2] == "#":
                answer.append(8)
                i += 3
            elif arr[1][i] == "#" and arr[2][i] == "#" and arr[3][i] == "#" and arr[4][i] == "#":
                answer.append(1)
                i += 1
        else:
            if arr[1][i] == "#" and arr[2][i] == "#" and arr[3][i] == "#" and arr[4][i] == "#":
                answer.append(1)
                i += 1
    else:
        i += 1
print("".join(map(str, answer)))            



'''
###..#..
#.#..#..
###..#..
#.#..#..
###..#..
'''

'''
###.#
#.#.#
###.#
#.#.#
###.#
'''

'''
#..###...#..#.#.
#..#.#...#..#.#.
#..#.#...#..#.#.
#..#.#...#..#.#.
#..###...#..#.#.
'''

'''
35

#.#.###
#.#.#..
###.###
..#...#
..#.###

'''
#틀렸던 이유 : 4와 9를 바꿔적음, 1이 맨 끝에오는 경우를 고려안해줌.