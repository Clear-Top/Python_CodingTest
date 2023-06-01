def solution(sizes):
    x = [garo[0] for garo in sizes]
    y = [sero[1] for sero in sizes]
    max_x = []
    max_y = []
    for g,s in zip(x,y):
        if (g>=s):
            max_x.append(g)
            max_y.append(s)
        else:
            max_x.append(s)
            max_y.append(g)
        
    return max(max_x) * max(max_y)
        


print(solution([[1, 1], [1, 1], [1, 1], [1, 1]]))