import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sumV = 0
    maxV = 0

#col 별 최대값 구하기
for row in range(100):
    sumV = 0
    for col in range(100):
        sumV += arr[row][col]
    if sumV > maxV:
        maxV = sumV

#row별 최댓값
for col in range(100):
    sumV = 0
    for row in range(100):
        sumV += arr[row][col]
    if sumV > maxV :
        maxV= sumV

#대각선 우
sumV = 0
for i in range(100):
    sumV += arr[i][i]
if sumV > maxV :
    maxV = sumV

#대각선 좌
sumV = 0
for i in range(100):
    sumV += arr[i][99-i]
if sumV > maxV:
    maxV = sumV

print(f'{tc} {maxV}')