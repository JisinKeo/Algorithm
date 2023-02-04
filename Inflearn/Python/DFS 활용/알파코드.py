def DFS(v, p):

    global cnt

    if v == n:
        cnt += 1
        for i in range(p):
            print(chr(64+result[i]), end='')
        print()

    else:
        for i in range(1, 27):
            if code[v] == i:
                result[p] =  i
                DFS(v+1, p+1)
            elif i>=10 and code[v] == i//10 and code[v+1] == i%10:
                result[p] = i
                DFS(v+2, p+1)

if __name__=="__main__":
    code = list(map(int, input()))
    n = len(code)

    result = [0] * (n)
    code.insert(n, -1)

    cnt = 0

    DFS(0, 0)

    print(cnt)
