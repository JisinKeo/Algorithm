import heapq

def solution(scoville, K):
    
    heapq.heapify(scoville)
    
    answer = 0
    
    while True:
        
        if scoville[0] >= K:
            break
        if len(scoville) == 1:
            temp = heapq.heappop(scoville)
            if temp < K:
                return -1
        
        temp = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, temp + temp2 * 2)
        
        answer += 1
        
    return answere
