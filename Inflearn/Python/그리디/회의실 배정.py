n = int(input())
number = []
for i in range(n):
    s, e = map(int, input().split())
    number.append((s,e))

number.sort(key = lambda x: (x[1], x[0]))

count = 0
end_time = 0


for s, e in number:
    if s>=end_time:
        end_time = e
        count+=1

print(count)
