'''
방법1: list로 변환한후, reverse()
방법2: 슬라이싱으로 뒤집기
'''
def solution(my_string, n):
    answer = my_string[-n:]
    print(f"my_string: {my_string}")
    print(f"answer: {answer}")
    return answer

# my_string = "ProgrammerS123" # n = 11
my_string = "He110W0r1d" # n = 5

# answer = solution(my_string, 11)
answer = solution(my_string, 5)
print(answer)