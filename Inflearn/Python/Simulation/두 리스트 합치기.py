import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())
lista = list(map(int, input().split()))
m = int(input())
listb = list(map(int, input().split()))
listc = []
i = 0
j = 0
k = 0
while True:   
    if lista[i] < listb[j]:
        listc.append(lista[i])
        i += 1
        k += 1
    elif lista[i] >= listb[j]:
        listc.append(listb[j])
        j += 1
        k += 1
    if i == len(lista) or j == len(listb):
        break

if i != len(lista):
    for p in range(i, len(lista)):
        listc.append(lista[p])
if j != len(listb):
    for p in range(j, len(listb)):
        listc.append(listb[p])
print(*listc)
