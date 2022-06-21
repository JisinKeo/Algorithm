def solution(n, times):
    
    lt = 1
    rt = n * max(times)
    
    while lt <= rt:
        mid = (lt+rt) // 2
        cnt = 0
        for x in times:           
            cnt += mid // x
    
        if cnt >= n:
            rt = mid - 1

        else:
            lt = mid + 1

    answer = lt
    return answer
