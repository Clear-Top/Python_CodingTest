def solution(array, commands):
    result = []
    for command in commands:
        # command: i, j, k (list)
        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        result.append(temp[k-1])
    return result

if __name__=="__main__":
    result = solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    
    print(*result)