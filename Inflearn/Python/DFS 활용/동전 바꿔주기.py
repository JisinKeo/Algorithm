def DFS(v, sum):

    global cnt

    if sum > t:
        return
    
    if v == k:
        if sum == t:
            cnt += 1
        return

    for i in range(0, num[v]+1):
        DFS(v+1, sum + pay[v]*i)


if __name__=="__main__":
    t = int(input())
    k = int(input())

    pay = []
    num = []
    
    for _ in range(k):
        p, n = map(int, input().split())
        pay.append(p)
        num.append(n)

    cnt = 0

    DFS(0, 0)

    print(cnt)
