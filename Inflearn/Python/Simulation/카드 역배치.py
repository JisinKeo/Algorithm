import sys
#sys.stdin = open("input.txt", "rt")
card =[]
for i in range(21):
    card.append(i)
for i in range(10):
    start, end = map(int, input().split())
    while(start<end):
        card[start], card[end] = card[end], card[start]
        start += 1
        end -= 1
for i in range(1, 21):
    print(card[i], end=' ')
    
