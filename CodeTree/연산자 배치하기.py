import sys

def DFS(v, num):
    global min_result, max_result, result
    if v == n:
        result.append(num)
        return
    
    for c in range(len(calculator)):
        if calculator[c] != 0:
            calculator[c] -= 1
            if c == 0:
                DFS(v+1, num + number[v])
            elif c == 1:
                DFS(v+1, num - number[v])
            else:
                DFS(v+1, num * number[v])
            calculator[c] += 1


n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))

calculator = list(map(int, sys.stdin.readline().split()))

result = []

DFS(1, number[0])

print(min(result), max(result))
