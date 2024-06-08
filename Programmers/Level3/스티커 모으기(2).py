def solution(sticker):
    answer = 0
    
    n = len(sticker)
    


    dp = [0] * n
    
    # 맨 처음 숫자 선택 
    
    dp[0] = sticker[0]
    
    dp[1] = sticker[1]
    
    dp[2] = sticker[2] + dp[0]
    
    for i in range(3, n-1):   
        dp[i] = max(dp[i-2], dp[i-3]) + sticker[i]
        
    first_choose = max(dp)
    
    # 맨 처음 숫자 선택 X
    
    dp = [0] * n
    
    dp[1] = sticker[1]
    
    dp[2] = sticker[2]
    
    for i in range(3, n):
        dp[i] = max(dp[i-2], dp[i-3]) + sticker[i]
        
    first_not_choose = max(dp)
    
    answer = max(first_choose, first_not_choose)

    return answer
