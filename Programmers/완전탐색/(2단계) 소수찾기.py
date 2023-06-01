from itertools import combinations, chain

def prime_check(number):
    print(number)
    answer = []
    for num in number:
        for i in range(2,int(num)):
            if int(num) % i == 0:
                return False
        answer.append(int(num))
    return answer

def solution(numbers):
    """
    1. 조합으로 만들고나서
    2. 소수 체크
    
    Prime Number = '2','3','5','7',1'1',1'3',1'7',1'9',2'3',2'9',3'1',3'7' ...
    
    끝자리가 2,3,5,7,1,9 인 것들중에서만 고려
    """
    num = list(numbers)

    result = []
    for i in range(1, len(num) + 1):
        # print(f"{i} 개 뽑아서 조합하기")
        result.append(list(map(list, combinations(num,i))))
    print(result)

    result2 = set()
    for i in range(len(result)):
        # print(result[i])
        result2.add("".join(chain(*result[i])))
    return len(prime_check(result2))

print(solution("17"))
print(solution("011"))