def solution(quiz):
    equations = []
    answer = []
    for equ in quiz:
        equations = equ.split("=")
        if eval(equations[0]) == int(equations[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["3 - 4 = -3", "5 + 6 = 11"]))
print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))