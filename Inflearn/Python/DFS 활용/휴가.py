def DFS(v, totalPeriod):

    global result

    if v + time[v] >= n:
        if v + time[v] == n:
            totalPeriod += period[v]
        if totalPeriod > result:
            result = totalPeriod
        return
    else:
        if v + time[v] <= n+1:
            DFS(v + time[v], totalPeriod + period[v])
        DFS(v+1, totalPeriod)
        
        



if __name__=="__main__":

    n = int(input())

    time = []
    period = []

    result = 0

    for _ in range(n):
        t, p = map(int, input().split())
        time.append(t)
        period.append(p)

    DFS(0, 0)

    print(result)


    
