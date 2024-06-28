from collections import Counter

def solution(a):
    answer = -1
    
    count = Counter(a)
    max_length = 0

    for num in count:
        if count[num] * 2 <= max_length:
            continue        
        length = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] == num or a[i + 1] == num) and a[i] != a[i + 1]:
                length += 2
                i += 2
            else:
                i += 1
                
        max_length = max(max_length, length)
    
    return max_length
