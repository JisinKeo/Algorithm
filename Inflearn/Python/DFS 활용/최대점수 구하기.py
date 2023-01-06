

def DFS(v, totalScore, totalTime):
    
    global result
        
    if totalTime > m:
        return
    
    if v == n:
        if totalScore > result:
            result = totalScore
        return


    DFS(v+1, totalScore + score[v], totalTime + time[v])
    DFS(v+1, totalScore, totalTime)
    



if __name__=="__main__":
    n, m = map(int, input().split())
    score = []
    time = []

    result = 0
    
    for _ in range(n):
        a, b = map(int , input().split())
        score.append(a)
        time.append(b)

    DFS(0, 0, 0)

    print(result)

