import sys

n = int(input())

customer = list(map(int, input().split()))

ldr, mbr = map(int, input().split())

cnt = 0

for i in range(len(customer)):
    customer[i] = customer[i] - ldr
    if customer[i] < 1:
        cnt += 1
    else:
        cache = customer[i] // mbr
        if customer[i] % mbr > 0:
            cache += 1
        cnt += (cache + 1)
print(cnt)
