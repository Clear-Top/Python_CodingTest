def solution(numbers, direction):
    if direction == "right":
        answer = numbers[:-1]
        return [numbers[-1]] + answer
    elif direction == "left":
        answer = numbers[1:]
        # print(answer)
        return answer + [numbers[0]]


# print(solution([1, 2, 3], "right"))
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))

""" 다른풀이 '덱' 으로 rotate 함수사용
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction == 'right':
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
"""
