n = int(input())

fruit = [list(map(int, input().split())) for _ in range(n)]
temp = n//2
result = 0
for i in range(n):
    if i<=temp:
        for j in range(temp-i, temp+i+1):
            result += fruit[i][j]
    else:
        a = (n-1)-i
        for j in range(temp-a, temp+a+1):
            result += fruit[i][j]
print(result)
