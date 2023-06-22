#O
def solution(numbers, hand):
    answer = ''
    leftHand = '*'
    rightHand = '#'
    phone = {'1': (0, 0), '2': (0, 1), '3': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '7': (2, 0), '8': (2, 1), '9': (2, 2), '*': (3,0), '0': (3, 1), '#': (3, 2)}
    for number in numbers:
        numStr = str(number)
        if number == 1 or number == 4 or number == 7:
            leftHand = numStr
            answer += 'L'
        elif number == 3 or number == 6 or number == 9:
            rightHand = numStr
            answer += 'R'
        else:
            leftDiff = abs(phone[leftHand][0] - phone[numStr][0]) + abs(phone[leftHand][1] - phone[numStr][1])
            rightDiff = abs(phone[rightHand][0] - phone[numStr][0]) + abs(phone[rightHand][1] - phone[numStr][1])
            if leftDiff < rightDiff:
                leftHand = numStr
                answer += 'L'
            elif leftDiff > rightDiff:
                rightHand = numStr
                answer += 'R'
            else:
                if hand == 'left':
                    leftHand = numStr
                    answer += 'L'
                else:
                    rightHand = numStr
                    answer += 'R'
    return answer