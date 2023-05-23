for test_num in range(10):
    dumpCnt = int(input())
    arr = list(map(int, input().split()))
    diff = 0
    while True:
        maxArr = max(arr)
        minArr = min(arr)
        diff = maxArr - minArr
        if dumpCnt == 0:
            break
        #평탄화 완료
        if diff <= 1:
            break
        higherIndex = 0
        lowerIndex = 0
        # 가장 높은곳, 낮은곳에 있는 상자 찾기
        for i in range(100):
            if arr[higherIndex] < arr[i]:
                higherIndex = i
            if arr[lowerIndex] > arr[i]:
                lowerIndex = i

        # 가장 높은곳에 있는 상자 가장 낮은곳으로 옮기기
        arr[higherIndex] -= 1
        arr[lowerIndex] += 1
        #덤프횟수 빼기
        dumpCnt -= 1
        
    # 덤프횟수 다 썼을때 최고점과 최저점을 찾아서 차이를 구하기
    print(f'#{test_num + 1} {diff}')
        