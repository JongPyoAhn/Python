def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0: #짝수
            answer.append(number ^ 1 << 0)
        else:#홀수
            number_bin = '0' + bin(number)[2:]
            number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0') + 2:]
            answer.append(int(number_bin, 2))
    return answer
print(solution([2, 15]))

