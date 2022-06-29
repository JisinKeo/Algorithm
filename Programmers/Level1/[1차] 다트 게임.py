def solution(dartResult):
    
    answer = []
    check = 0
    for x in dartResult:
        if x >= '0' and x<= '9':
            if check == 1 and x == '0':
                temp = 10
            else:
                if x == '1':
                    temp = int(x)
                    check = 1
                else:
                    temp = int(x)
        elif x == 'S':
            check = 0
            answer.append(temp)
        elif x == 'D':
            check = 0
            answer.append(temp * temp)
        elif x == 'T':
            check = 0
            answer.append(temp * temp * temp)
        elif x == '*':
            check = 0
            if len(answer) == 1:
                temp = answer.pop()
                answer.append(temp*2)
            else:
                answer[-2] *= 2
                answer[-1] *= 2
            
        elif x == '#':
            check = 0
            temp = answer.pop()
            answer.append(temp * (-1))
    return sum(answer)
