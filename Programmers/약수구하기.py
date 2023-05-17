def solution(num, k):
    try:
        num_list = [int(i) for i in str(num)]
        return num_list.index(k) + 1
    except:
        return -1


print(solution(29183, 1))
