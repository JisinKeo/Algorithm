def solution(d, budget):
    
    d.sort()
    
    total = 0
    cnt = 0 
    
    for x in d:
        total += x
        if total>budget:
            break
        cnt += 1
    answer = cnt
    return answer
