def transformDay(str):
    splited = list(map(int, str.split('.')))
    year = splited[0] * 12 * 28
    month = splited[1] * 28
    day = splited[2]
    return year + month + day

def solution(today, terms, privacies):
    transforemdToday = transformDay(today)
    dict = {}
    result = []
    for term in terms:
        splited = term.split(' ')
        dict[splited[0]] = int(splited[1]) * 28
    
    for i, privacie in enumerate(privacies):
        splited = privacie.split()
        if transforemdToday - transformDay(splited[0]) >= dict[splited[1]]:
            result.append(i + 1)
    
    answer = result
    return answer