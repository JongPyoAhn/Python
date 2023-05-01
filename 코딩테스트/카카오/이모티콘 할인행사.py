
totalSales = [[]]
result = []
def dfs(depth, sales, emoticons):
    if depth == len(emoticons):
        totalSales.append(result[:])
        return
    
    for i in range(len(sales)):
        result.append(sales[i])
        dfs(depth + 1, sales, emoticons)
        result.pop()
    
def solution(users, emoticons):
    sales = [10, 20, 30, 40]
    dfs(0, sales, emoticons)
    answer = [0, 0]
    
    for i in range(1, len(totalSales)):
        emoticonPlus = 0
        totalSum = 0
        for user in users: #[[40, 10000], [25, 10000]]
            sum = 0
            for j in range(0, len(totalSales[i])):
                if user[0] <= totalSales[i][j]:
                    sum += emoticons[j] - (emoticons[j] * totalSales[i][j] * 0.01)
                    if sum >= user[1]:
                        emoticonPlus += 1
                        totalSum -= sum
                        break
                    
            totalSum += sum
            
        if emoticonPlus > answer[0]:
            answer = [emoticonPlus, int(totalSum)]
        elif emoticonPlus == answer[0]:
            if totalSum > answer[1]:
                answer = [emoticonPlus, int(totalSum)]
        
    return answer
users = [[40, 10000], [25, 10000]]	
emoticons = [7000, 9000]
print(solution(users, emoticons))