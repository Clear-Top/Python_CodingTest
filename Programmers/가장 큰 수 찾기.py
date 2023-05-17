def solution(array):
    max_num = max(array)
    index = array.index(max(array))  # .find()는 문자열함수
    return [max_num, index]


print(solution([1, 8, 3]))
