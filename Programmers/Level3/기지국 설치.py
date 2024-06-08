def solution(n, stations, w):
    
    answer = 0
    
    start = 1
    
    distance = 2 * w + 1
    
    for station in stations:
        if start < station - w:
            answer += (station - w - start) // distance
            if (station - w - start) % distance > 0:
                answer += 1
        start = station + w + 1

            
    if start <= n:
        answer += (n + 1 - start) // distance
        if (n + 1 - start) % distance > 0:
            answer += 1    

    return answer
