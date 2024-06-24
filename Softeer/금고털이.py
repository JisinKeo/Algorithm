import sys

W, N = map(int, input().split())
items = []
for _ in range(N):
    Mi, Pi = map(int, input().split())
    items.append((Mi, Pi))

items.sort(key=lambda x: x[1], reverse=True)

result = 0
weight = 0

for Mi, Pi in items:
    if weight < W:
        if weight + Mi <= W:
            result += (Mi * Pi)
            weight += Mi
        else:
            if W - weight <= Mi:
                result += ((W - weight) * Pi)
                break
            else:
                result += (Mi * Pi)
                weight += Mi

print(result)
        
        
