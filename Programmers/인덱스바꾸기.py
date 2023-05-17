def solution(my_string, num1, num2):
    ch1 = my_string[num1]
    ch2 = my_string[num2]

    # print(ch1, ch2)

    answer = ""

    answer += "".join(my_string[:num1])
    answer += ch2
    answer += "".join(my_string[num1 + 1 : num2])
    answer += ch1
    answer += "".join(my_string[num2 + 1 :])

    return answer
    # print(my_string[:num1])
    # print(my_string[num1 + 1 : num2])
    # print(my_string[num2 + 1 :])
    # my_string[num1] = ch2

    # return my_string


print(solution("I love you", 3, 6))


""" 다른풀이 swap
def solution(my_string, num1, num2):
    s = list(my_string)
    s[num1],s[num2] = s[num2],s[num1]
    return ''.join(s)
"""
