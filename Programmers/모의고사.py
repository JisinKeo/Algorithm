def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    one_cnt = 0
    two_cnt = 0
    three_cnt = 0
    
    for i in range(0, len(answers)):
        if answers[i] == one[i%5]:
            one_cnt+=1
    
    for i in range(0, len(answers)):
        if answers[i] == two[i%8]:
            two_cnt+=1            
        
    for i in range(0, len(answers)):
        if answers[i] == three[i%10]:
            three_cnt+=1
    
    temp = max(one_cnt, two_cnt, three_cnt)
    
    if temp == one_cnt:
        answer.append(1)
    if temp == two_cnt:
        answer.append(2)
    if temp == three_cnt:
        answer.append(3)
        

    return answer
