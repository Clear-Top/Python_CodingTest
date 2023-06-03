
def solution(n, lost, reserve):
    union = set(lost + reserve)
    filter_lost = list(union - set(reserve))
    filter_reserve = list(union - set(lost))
    num_fail_student = len(filter_lost)

    for student in filter_lost:
        # print(f"{student} 학생이 돌아다닙니다.")
        if student - 1 in filter_reserve:
            # print(f"{student}는 {student-1}에게 체육복을 빌렸습니다.")
            filter_reserve.remove(student-1)
        elif student + 1 in filter_reserve:
            # print(f"{student}는 {student+1}에게 체육복을 빌렸습니다.")
            filter_reserve.remove(student+1)
        else:   # 빌려받을 수가 없음
            continue
        num_fail_student -= 1
        # print(f"현재 체육복 빌릴 수 있는지 물어봐야할 학생들은 {filter_lost}입니다. ")
    return n - num_fail_student

# n, lost, reserve
print(solution(30, [1,30], [2,29]))  
print(solution(30, [2,29], [1,30]))  
print(solution(4, [2,4], [1,3]))
print(solution(4, [1,3], [2,4]))