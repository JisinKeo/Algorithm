def solution(n):
    global answer
    answer = ''    

    i = 1
    while True:
        if 3*(3**(i-1)-1)/2<= n and n<=3*(3**i-1)/2:
            break
        i += 1

    while True:
        if i==0:
            break
        else:
            if n % 3 == 1:
                answer += '1'
                n = n//3
                i = i-1
            elif n % 3 == 2:
                answer += '2'
                n = n//3
                i -= 1
            elif n % 3 == 0:
                answer += '4'
                n = n//3-1
                i -= 1

    
    answer = "".join(reversed(answer))
    
    return answer
