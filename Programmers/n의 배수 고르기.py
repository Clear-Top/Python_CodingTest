def solution(n, numlist):
    return [i for i in numlist if i % n == 0]


print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))

"""다른 풀이
def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))
"""
