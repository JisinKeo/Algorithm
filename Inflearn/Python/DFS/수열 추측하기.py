import sys

def DFS(v, sum):

    if v == n:
        if sum == f:
            print(result)
            sys.exit(0)

    else:
        for i in range(1, n+1):
            if checked[i] == 0:
                checked[i] = 1
                result[v] = i
                DFS(v+1, sum + (bc[v] * result[v]))
                checked[i] = 0
                







if __name__ == "__main__":
 
    n, f = map(int, input().split())

    result = [0] * n

    checked = [0] * (n+1)

    numerator = [1] * n

    denumerator = [1] * n

    bc = [1] * n

    for i in range(1, n):
        numerator[i] = numerator[i-1] * (n-i)

    for j in range(1, n):
        denumerator[j] = denumerator[j-1] * j


    for k in range(1, n):
        bc[k] = numerator[k] // denumerator[k]


    for i in range(1, n+1):

        DFS(0, 0)



    
