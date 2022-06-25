def solution(N, stages):
    
    answer = []
    dict = {}
    
    for n in range(1, N+1):
        
        cnt = 0
        total = 0
        for i in range(0, len(stages)):

            if stages[i]>=n:
                total+=1
                if stages[i]<=n:
                    cnt+=1
        if total == 0:
            dict[n] = 0
        else:
            dict[n] = cnt/total            
    
    dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)


    for key,value in dict:
        answer.append(key)
                
    
    return answer
