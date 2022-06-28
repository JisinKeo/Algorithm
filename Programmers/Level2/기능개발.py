def solution(progresses, speeds):
    answer = []
    
    day = []
    length = len(progresses)
    
    for i in range(length):
        cnt = 0
        while True:
            if progresses[i] >= 100:
                day.append(cnt)
                break
            progresses[i] += speeds[i]
            cnt += 1
    count = 0
    k = 0
    for i in range(0, len(day)-1):
        if day[k]>=day[i+1]:
            count += 1
        elif day[k] < day[i+1]:
            answer.append(count+1)
            k = i+1
            count = 0
                    
    answer.append(count+1)
    return answer
