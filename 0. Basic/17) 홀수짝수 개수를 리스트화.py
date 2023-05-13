''' 다른 풀이 1
def solution(num_list):
    div_num_list = list(map(lambda v: v % 2, num_list))
    return [div_num_list.count(0), div_num_list.count(1)]
'''
'''다른 풀이 2 (Best)
def solution(num_list):
    answer = [0,0]
    for n in num_list:
        answer[n%2]+=1
    return answer
'''

# def solution(num_list=[1, 2, 3, 4, 5]):
#     answer = list()
#     odd = list(filter(lambda x:x%2!=0, num_list))
#     even = list(filter(lambda x:x%2==0, num_list))
#     answer.append(len(odd))
#     answer.append(len(even))
#     print(answer)
    
# solution()

def solution (num_list=[1, 2, 3, 4, 5]):
    even = []
    odd = []
    for elem in num_list:
        if elem%2==0:
            even.append(elem)
        else:
            odd.append(elem)
    return [len(even), len(odd)]

print(solution())