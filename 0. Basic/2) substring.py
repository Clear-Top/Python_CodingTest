def solution(my_string, target):
    '''
    .find()함수사용
    1. 부분문자열이라면 일치하는 시작 index
    2. 부분문자열이 아니라면, -1을 리턴함
    '''
    flag = 'No' if len(my_string) < len(target) else 'Yes'
    if flag == 'Yes':
        index = my_string.find(target)
        answer = 1 if index!=-1 else 0
    else:
        answer = 0
    return answer

str1, str2 = input().split()

answer = solution (str1, str2)
print(answer)