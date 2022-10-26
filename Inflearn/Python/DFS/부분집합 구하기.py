def DFS(v):
    if v == n+1:
        for i in range(1, n+1):
            if check[i] == 1:
                print(i, end = ' ')
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n+1)
    DFS(1)
    
