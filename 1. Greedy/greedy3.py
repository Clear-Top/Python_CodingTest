'''
문제: 각 자리가 숫자 (0부터 9)로만 이루어진 문자열이 주어졌을때,
    왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인해가며 '+' 혹은 '*' 연산자를 넣어서
    만들어질 수 있는 가장 큰 수를 구하는 프로그램 작성

입력: 첫째 줄에 여러개의 숫자로 구성된 하나의 문자열이 주어진다 (길이: 1~20)
출력: 계산된 가장 큰 수를 출력

시간: 1초
메모리: 128MB
'''

# 아이디어
# 두 수 중 하나가 0이라면? => 곱하기보다 더하기가 good!
# 두 수 중 하나가 1이라면? => 곱하기보다 더하기가 good!

# 최대 길이가 20인 문자열 입력

import time

def greedy3():
    result = int(str[0])
    for i in range(1,len(str)):
        operand = int(str[i])
        if result <=1  or operand <= 1:
            result += operand
            continue
        result *= operand
    return result

str = input()
start = time.time()

result = greedy3()
print(result)

end = time.time()

print(f"{end-start:.3f} seconds")
