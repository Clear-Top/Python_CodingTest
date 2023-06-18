def solution(input_string):
    item_set = set(input_string)
    # print(f'item_set = {item_set}')
    # print(input_string.find(item))
    answer = []
    for item in item_set:
        start = input_string.find(item)
        for idx in range(start+1, len(input_string)):
            if input_string[idx] == item:
                answer.append(item)
                break
                
    return "".join(answer)

print(solution("edeaaabbccd"))
# print(solution("eeddee"))
# print(solution("string"))
# print(solution("zbzbz"))