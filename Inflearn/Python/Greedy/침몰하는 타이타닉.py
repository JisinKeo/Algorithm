n, m = map(int, input().split())

weight = list(map(int, input().split()))

weight.sort()

cnt = 0

while weight:
    if len(weight)<=1:
        weight.pop()
        cnt += 1
    else:
        if weight[0]+weight[-1]>m:
            weight.pop()
            cnt += 1
        else:
            weight.pop(0)
            weight.pop()
            cnt += 1

print(cnt)

