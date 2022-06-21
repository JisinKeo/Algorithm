
def solution(numbers, target):
    global cnt, total
    total = 0
    cnt = 0 
    def DFS(index, total):
        global cnt
        if index == len(numbers)-1:
            if total == target:
                cnt += 1
            return 
        index += 1
        DFS(index, total+numbers[index])
        DFS(index, total-numbers[index])
        
        

    DFS(-1, 0)
    
    answer = cnt
    return answer
