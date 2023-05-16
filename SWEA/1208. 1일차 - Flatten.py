for testcase in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))
    
    for _ in range(dump):    
        height[height.index(max(height))] -= 1
        height[height.index(min(height))] += 1
    print('#%d %d'%(testcase, max(height)-min(height)))
