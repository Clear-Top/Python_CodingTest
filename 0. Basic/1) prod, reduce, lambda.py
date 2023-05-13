# from math import prod

# def solution(num_list):
#     answer = prod(num_list)
#     return answer

# num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
# num_list = [2, 3, 4, 5]

# print(solution(num_list))

from functools import reduce
'''

'''
def solution(num_list):
    if len(num_list) >= 11:
        answer = reduce((lambda x, y: x+y), num_list)
    else:
        answer = reduce((lambda x, y: x*y), num_list)
    return answer

# num_list = [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]
num_list = [2, 3, 4, 5]
answer = solution(num_list)
print(answer)