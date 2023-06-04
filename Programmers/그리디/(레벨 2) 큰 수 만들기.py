def pop_number(new_number, target_number, k):
    """
    new_number의 꼭대기값이 number[target_index] 보다 크거나 같을때까지 pop하기
    """
    while len(new_number) > 0 and k>0 and new_number[-1] < target_number:
        new_number.pop()
        k -= 1
    return k

def solution(number, k):
    """
    [parameters]
    number  : 원본 수
    k       : 제거할 숫자의 수

    [variables]
    new_number : k 개의 숫자가 제거된 수(answer)
    """
    # 하나는 넣고 시작
    new_number = [number[0]]
    target_index = 1

    while target_index<len(number):
        if new_number[-1]<number[target_index] and k > 0:
            k = pop_number(new_number, number[target_index], k)
        new_number.append(number[target_index])
        target_index += 1
    
    # 추가
    while k != 0:
        new_number.pop()
        k-=1
    return "".join(new_number)

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("91", 1))