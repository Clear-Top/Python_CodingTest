''' 다른 풀이
def solution(my_string):
    return my_string[::-1]
'''

# def solution(my_string="jaron"):
#     answer = list(reversed(my_string))
#     return ''.join(answer)

# print(solution())

my_string = "hello"

print(type(my_string[:3]))
print(type(my_string[::-1]))
print(type(my_string[1:3]))