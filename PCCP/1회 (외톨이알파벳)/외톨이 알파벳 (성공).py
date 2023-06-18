def solution(input_string):
    answer = ''
    dic = {}
    answer_list = []
    # for idx, alpha in enumerate(input_string):
    #     if alpha not in count:
    #         count[alpha] = [idx]
    #     else:
    #         count[alpha].append(idx)

    for idx, c in enumerate(input_string):
        dic.setdefault(c, [])
        dic[c].append(idx)

    print(dic)
    
    for key, value in dic.items():
        if len(value) >= 2: # 조건1
            for i in range(len(value) - 1):
                if abs(value[i]-value[i+1]) > 1: # 조건2
                    answer_list.append(key)
                    break

    if len(answer_list) == 0:
        answer = "N"
    else:
        answer = ''.join(sorted(answer_list))
        
    return answer

print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))