from itertools import permutations

def solution(numbers):
    temp = []
    result = set()
    for x in numbers:
        temp.append(x)
    
    for x in range(1, len(temp)+1):
        for j in permutations(temp,x):
            tmp = "".join(j)
            tmp = int(tmp)
            if tmp < 2:
                continue
            else:
                check = 0
                for k in range(2,int(tmp**0.5) + 1):
                    if tmp % k == 0:
                        check = 1
        
                if check == 0:
                    result.add(tmp)

    answer = len(result)
    return answer
