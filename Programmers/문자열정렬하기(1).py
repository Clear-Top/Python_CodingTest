def solution(my_string):
    try:
        return sorted(
            list(map(int, (filter(lambda x: x.isdigit(), [i for i in my_string]))))
        )
    except:
        pass


# print(solution("hi12392"))
print(solution("p2o4i8gj2"))
# print(solution("abcde0"))

""" 나랑 유사한 풀이
def solution(my_string):
    return sorted(map(int, filter(lambda s: s.isdigit(), my_string)))
"""

""" 다른 풀이
def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
"""
