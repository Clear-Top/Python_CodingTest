'''
번호가 낮은 프로그램이 실행우선순위가 높다
그러나, 먼저도착한 프로그램이 실행된다.
'''

''' 출력
answer[0] = 모든 프로그램 종료시간
answer[k] (1<=k<=11) = 프로그램 점수별 대기시간 총합
'''

''' 효율성 측면
프로그램의 길이 = 100,000 => O(nlogn)
'''
from collections import deque
def solution(program):
    program.sort(key = lambda x:(x[1], x[0]))
    current_time = 0
    q = deque(program)
    # print(q)
    current_time = 0
    answer = [0] * 11
    target_program = 0
    while q:
        if q[0][1]<=current_time:
            exe = q.popleft()
            # target_program += 1
        else:
            current_time += 1
            continue
        # exe = q.popleft()
        answer[exe[0]] += (current_time-exe[1])
        current_time += exe[2]
    answer[0] = current_time

    print(answer)
    
    return 

# [a,b,c] : [우선순위, 도착시간, 실행시간]
# print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]])) # [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]

print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
