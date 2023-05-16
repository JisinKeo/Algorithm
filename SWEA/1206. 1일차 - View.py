for testcase in range(1, 11):

    n = int(input())

    aparts = list(map(int, input().split()))

    sum = 0

    for i in range(n):

        if i == 0:
            if aparts[0] > aparts[1] and aparts[0] > aparts[2]:
                apart = max(aparts[1], aparts[2])
                sum += aparts[0] - apart

        elif i == n-1:
            if aparts[n-1] > aparts[n-2] and aparts[n-1] > aparts[n-3]:
                apart = max(aparts[n-2], aparts[n-3])
                sum += aparts[n-1] - apart

        else:
            if aparts[i] > aparts[i-1] and aparts[i] > aparts[i-2] and aparts[i] > aparts[i+1] and aparts[i] > aparts[i+2]:
                apart = max(aparts[i-1], aparts[i-2], aparts[i+1], aparts[i+2])     
                sum += aparts[i] - apart
    print('#%d %d'%(testcase, sum))
