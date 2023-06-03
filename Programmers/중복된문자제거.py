def solution(my_string):
    """
    1. 앞에서 하나씩 꺼내서 결과변수에 있는지 확인
    2. 결과변수에 있다면 넣고, 없으면 냅두기
    """
    my_string_list = list(my_string)
    result_list = []

    for c in my_string_list:
        if not c in result_list:
            result_list.append(c)
    return "".join(result_list)
        
    # print(type(result_set))

print(solution("people"))
print(solution("We are the world"))