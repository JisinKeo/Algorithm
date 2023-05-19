n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n+1)
dy[1] = 1
result = 0
for i in range(2, n+1):
    max_num = 0
    for j in range(0, i):
        if dy[j] > max_num and arr[i] > arr[j]:
            max_num = dy[j]
    dy[i] = max_num + 1

print(max(dy))
