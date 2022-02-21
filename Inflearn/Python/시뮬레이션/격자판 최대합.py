'''
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.
▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50) 
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다. 
▣ 출력설명
최대합을 출력합니다.
▣ 입력예제 1 
5
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
▣ 출력예제 1
155
'''

import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
number = [list(map(int, input().split())) for _ in range(n)]

max1 = 0
for i in range(n):
    sum1 = 0
    for j in range(n):
        sum1 += number[i][j]

    if sum1 > max1:
        max1 = sum1

for j in range(n):
    sum1 = 0
    for i in range(n):
        sum1 += number[i][j]

    if sum1 > max1:
        max1 = sum1
sum1 = 0
sum2 = 0
for i in range(n):
    sum1 += number[i][i]
    sum2 += number[n-(i+1)][i]
if sum1 > max1:
    max1 = sum1
if sum2 > max1:
    max1 = sum2
        
print(max1)
