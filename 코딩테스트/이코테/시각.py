# import sys
# si = sys.stdin.readline
# n = int(si())
# nTosec = ((n + 1) * 3600)

# def secToTime(sec):
#     s = sec
#     h = s // 3600
#     s -= (h * 3600)
#     m = s // 60
#     s -= (m * 60)
#     return f'{h}{m}{s}'
# answer = 0
# for i in range(nTosec):
#     times = secToTime(i)
#     for time in times:
#         if time == '3':
#             answer += 1
#             break
                
# print(answer)
    
# import sys
# si = sys.stdin.readline
# n = int(si())
# answer = 0
# for i in range(n + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 answer += 1
# print(answer)