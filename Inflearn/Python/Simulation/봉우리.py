n = int(input())

mountain = [list(map(int, input().split())) for _ in range(n)]

mountain.insert(0, [0]*n)
mountain.append([0]*n)

for x in mountain:
    x.insert(0, 0)
    x.append(0)

dx = [-1,0,1,0]
dy = [0,1,0,-1]
result = 0 
for i in range(1, n+1):
    for j in range(1, n+1):
        count = 0
        for k in range(4):
            if mountain[i][j] > mountain[i+dx[k]][j+dy[k]]:
                count += 1
        if count == 4:
            result += 1
print(result)
