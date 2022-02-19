'''
문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만
듭니다. 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
만약 “t0e0a1c2h0er”에서 숫자만 추출하면 0, 0, 1, 2, 0이고 이것을 자연수를 만들면 120이 
됩니다. 즉 첫 자리 0은 자연수화 할 때 무시합니다. 출력은 120를 출력하고, 다음 줄에 120
의 약수의 개수를 출력하면 됩니다.
추출하여 만들어지는 자연수는 100,000,000을 넘지 않습니다.
'''

import sys
#sys.stdin = open("input.txt", "rt")


string = input()
result = 0
for i in range(len(string)):
    if ord(string[i])>=48 and ord(string[i])<=57:
        result = result + (ord(string[i])-48);
        result *= 10
result /= 10
result = int(result)
count = 0
for i in range(1, result):
    if result % i == 0:
        count += 1
print(result)
print(count+1)
