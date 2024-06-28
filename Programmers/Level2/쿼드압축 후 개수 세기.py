def solution(arr):
    
    n = len(arr)
    
    def compress(x, y, size):
        num = arr[x][y]
        all_same = True
        
        for i in range(x, x + size):
            for j in range(y, y + size):
                if num != arr[i][j]:
                    all_same = False
                    break
            if not all_same:
                break
        
        if all_same:
            return (1, 0) if num == 0 else (0, 1) 
        
        top_left = compress(x, y, size // 2)
        top_right = compress(x, y + size // 2, size // 2)
        bottom_left = compress(x + size // 2, y, size // 2)
        bottom_right = compress(x + size // 2, y + size // 2, size // 2)
        
        
        return (top_left[0] + top_right[0] + bottom_left[0] + bottom_right[0],
                top_left[1] + top_right[1] + bottom_left[1] + bottom_right[1])

    return compress(0, 0, n)
