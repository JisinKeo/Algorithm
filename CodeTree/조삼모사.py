import sys
from itertools import combinations

def caculate_work(index):

    sum_work = 0

    for i in range(len(index)):
        for j in range(i+1, len(index)):
                sum_work += (work[index[i]][index[j]] + work[index[j]][index[i]])
    
    return sum_work

n = int(sys.stdin.readline())

work = []

for i in range(n):
    work.append(list(map(int, sys.stdin.readline().split())))

indices = list(range(n))
result = 1e9

for combi in combinations(indices, n//2):
    morning_index = list(combi)
    evening_index = [i for i in range(n) if i not in combi]        

    difference = abs(caculate_work(morning_index) - caculate_work(evening_index))
    result = min(result, difference)

print(result)
