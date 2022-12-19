
def DFS(v, start):
    global count
    
    if v == m:
        print(result)
        count+=1
        return

    else:
        for i in range(start, n+1):
            if chk[i] == 0:
                chk[i] = 1
                if v > 0 and i > result[v-1]:
                    result[v] = i
                elif v == 0:
                    result[v] = i
                DFS(v+1, i)
                chk[i] = 0

if __name__=="__main__":
    n, m = map(int, input().split())
    count = 0
    chk = [0] * (n+1)
    result = [0] * m
    DFS(0, 1)
    print(count)
