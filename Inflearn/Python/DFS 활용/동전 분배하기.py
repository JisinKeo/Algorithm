def DFS(v):
    global result
    if v == n:

        if result > max(person) - min(person):
            if person[0] != person[1] and person[1] != person[2] and person[0] != person[2]:
                result = max(person) - min(person)
        return

    for i in range(3):
        person[i] += coin[v]
        DFS(v+1)
        person[i] -= coin[v]

if __name__=="__main__":
    n = int(input())

    coin = []

    person = [0] * 3

    result = 10000000000

    for _ in range(n):
        c = int(input())
        coin.append(c)

    DFS(0)

    print(result)
