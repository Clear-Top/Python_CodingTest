from bisect import bisect_left, bisect_right


def solution(numbers):
    numbers.sort()  # -5 -3 1 2 4
    index = bisect_left(numbers, 0)

    left_list = numbers[:index]
    right_list = numbers[index:]

    if len(left_list) == 1 and len(right_list) == 1:
        return left_list[0] * right_list[0]
    elif len(left_list) < 2:
        return right_list[-1] * right_list[-2]
    elif len(right_list) < 2:
        return left_list[0] * left_list[1]
    else:
        return max(left_list[0] * left_list[1], right_list[-2] * right_list[-1])


print(solution([-1, 4]))


""" 다른풀이
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 
"""
