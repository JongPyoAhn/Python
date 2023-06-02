import sys
si = sys.stdin.readline
read = list(map(str, si().split()))
basicOperator = read[0]
for i in range(1, len(read)):
    curStr = read[i][:len(read[i]) - 1]
    temp = ""
    operTemp = ""
    for s in curStr:
        if s != "*" and s != "[" and s != "]" and s != "&":
            temp += s
        else:
            if s == "[":
                operTemp += "]"
            elif s == "]":
                operTemp += "["
            else:
                operTemp += s
    modified = "".join(list(reversed(operTemp)))
    print(f"{basicOperator}{modified} {temp};")
