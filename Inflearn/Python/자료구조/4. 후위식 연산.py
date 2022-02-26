'''
후위식 연산
후위연산식이 주어지면 연산한 결과를 출력하는 프로그램을 작성하세요.
만약 3*(5+2)-9 을 후위연산식으로 표현하면 352+*9- 로 표현되며 그 결과는 21입니다.
▣ 입력설명
첫 줄에 후위연산식이 주어집니다. 연산식의 길이는 50을 넘지 않습니다.
식은 1~9의 숫자와 +, -, *, /, (, ) 연산자로만 이루어진다.
▣ 출력설명
연산한 결과를 출력합니다.
▣ 입력예제 1 
352+*9-
▣ 출력예제 1
12
'''
import sys
#sys.stdin = open("input.txt", "rt")

string = input()

stack = []
result = 0
for cal in string:
    if ord(cal)>=48 and ord(cal)<=57:
        cal = int(ord(cal)-48)
        stack.append(cal)
    else:
        if cal == '+':
            temp = stack.pop()
            temp2 = stack.pop()
            temp3 = int(temp) + int(temp2)
            stack.append(temp3)
        elif cal == '-':
            temp = stack.pop()
            temp2 = stack.pop()
            temp3 = int(temp2) - int(temp)
            stack.append(temp3)
        elif cal == '*':
            temp = stack.pop()
            temp2 = stack.pop()
            temp3 = int(temp) * int(temp2)
            stack.append(temp3)
        else:
            temp = stack.pop()
            temp2 = stack.pop()
            temp3 = int(temp) // int(temp2)
            stack.append(temp3)

print(stack[0])
