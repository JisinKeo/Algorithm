L = int(input())

height = list(map(int, input().split()))

count = int(input())


height.sort()

for _ in range(count):
    height[0] += 1
    height[L-1] -= 1
    height.sort()


print(height[L-1]-height[0])
