def solution(my_string):
    answer = ""
    for i in my_string:
        if "a" <= i <= "z":
            answer += chr(ord("A") + ord(i) - ord("a"))
            # pass  # 대문자변환
        elif "A" <= i <= "Z":
            answer += chr(ord(i) - ord("A") + ord("a"))
            # pass  # 소문자변환
    return answer


# solution("cccCCC")
solution("abCdEfghIJ")

"""lower(), upper() 사용하기
def solution(my_string):
    answer = ''

    for i in my_string:
        if i.isupper():
            answer+=i.lower()
        else:
            answer+=i.upper()
    return answer
"""

"""swapcase() 사용하기
def solution(my_string):
    return my_string.swapcase()
"""
