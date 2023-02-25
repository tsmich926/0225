import sys
sys.stdin = open("input.txt", "r")

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]

    sumV = 0
    maxV = 0

    #col합의 최댓값 구하기
    for row in range(100):
        sumV = 0
        for col in range(100):
            sumV += arr[row][col]
        if sumV > maxV :
            maxV =sumV

    #row합의 최댓값 구하기
    for col in range(100):
        sumV = 0
        for col in range(100):
            sumV += arr[row][col]
        if sumV > maxV:
            maxV = sumV

    #대각선우
    sumV = 0 #!초기화 잊지 않기
    for i in range(100):
        sumV += arr[i][i]
    if sumV > maxV:
        maxV = sumV
    
    #대각선좌
    sumV = 0  #!초기화 잊지 않기
    for i in range(100):
        sumV += arr[i][99-i]
    if sumV > maxV :
        maxV = sumV

    print(f'#{tc} {maxV}')