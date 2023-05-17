"""
가위    : 2
바위    : 0 
보      : 5
"""


def solution(rsp):
    rock_scissor_paper = {"2": "0", "0": "5", "5": "2"}
    answer = ""
    for i in rsp:
        answer += rock_scissor_paper[i]
    return answer


print(solution("205"))
# print(solution("205"))
