def solution(input_string):

    # idea = input_string 에 존재하는 알파벳들의 index를 저장
    dic = {}   # key: alpha, value: list of indexes
    answer = []
    for idx, c in enumerate(input_string):
        dic.setdefault(c, [])
        dic[c].append(idx)
    
    for key, lst in dic.items():
        if len(lst) < 2:
            continue
        for i in range(len(lst) - 1):
            if lst[i+1] - lst[i] == 1:
                # 외톨이 알파벳아님
                break
            else:
                answer.append(key)
    if len(answer) != 0:
        answer.sort()
        return "".join(answer)
    else:
        return "N"


print(solution("edeaaabbccd"))
print(solution("eeddee"))
print(solution("string"))
print(solution("zbzbz"))