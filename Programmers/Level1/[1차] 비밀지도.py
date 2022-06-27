def solution(n, arr1, arr2):
    
    answer = [[2] * n for _ in range(n)]
    
    for i in range(0, len(arr1)):
        temp = n
        chk = 2 ** (temp-1)
        while arr1[i] > 0:
            if arr1[i] >= chk:
                answer[i][len(arr1) - temp] = 3
                arr1[i] -= chk
            temp -= 1
            chk /= 2
    for i in range(0, len(arr2)):
        temp = n
        chk = 2 ** (temp-1)
        while arr2[i] > 0:
            if arr2[i] >= chk:
                answer[i][len(arr2) - temp] = 3
                arr2[i] -= chk
            temp -= 1
            chk /= 2   
    
    ans = [''] * n
    for i in range(0, n):
        for j in range(0, n):
            if answer[i][j] == 3:
                ans[i] += '#'
            elif answer[i][j] == 2:
                ans[i] += ' '
        
    return ans
