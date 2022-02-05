h, m = map(int, input().split(" "))

if m < 45:
    if h == 0:
        h = 24

resultMinute = (((h * 60) + m) - 45)
print('{0} {1}'.format(int(resultMinute / 60), resultMinute % 60))