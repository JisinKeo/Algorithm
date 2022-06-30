def solution(rows, columns, queries):
    
    matrix = [[0]*columns for _ in range(rows)]
    k = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = k
            k += 1
    for i in range(0, len(queries)):
        for j in range(0, 4):
            queries[i][j] -= 1
            
    answer = []    
    
    for i in range(0, len(queries)): 
        cache = []
        a = queries[i][0]
        b = queries[i][1] 
        c = queries[i][2] 
        d = queries[i][3] 
        temp2 = matrix[a][d]
        cache.append(temp2)
        temp3 = matrix[c][b]
        cache.append(temp3)
        temp4 = matrix[c][d]
        cache.append(temp4)
        
        for q in range(d, b, -1):
            cache.append(matrix[a][q-1])
            matrix[a][q] = matrix[a][q-1]
            
        
        for p in range(c, a+1, -1):
            cache.append(matrix[p-1][d])
            matrix[p][d] = matrix[p-1][d]
            
        for q in range(b+1, d+1):
            cache.append(matrix[c][q])
            matrix[c][q-1] = matrix[c][q]
        
        for p in range(a+1, c+1):
            cache.append(matrix[p][b])
            matrix[p-1][b] = matrix[p][b]
            
        matrix[a+1][d] = temp2
        matrix[c-1][b] = temp3
        matrix[c][d-1] = temp4
        answer.append(min(cache))
                
    return answer
