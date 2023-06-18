from collections import deque
from heapq import heappush, heappop
def solution(program):
    '''
    1. program은 처음은 호출순서로 정렬
    2. 현재시간보다 작은거 program에서 pop하면서 우선순위 큐에 삽입 (점수오름차순)
    '''
    hq = []
    program.sort(key=lambda x:x[1])
    print(program)
    q = deque(program)
    current_time = 0
    answer = [0] * 11
    complete_pro = 0
    
    while complete_pro < len(program) or hq:
        # wait_time = 0
        while q and q[0][1] <= current_time :
            heappush(hq,q.popleft())
        if not hq and q[0][1] > current_time:
            current_time += q[0][1] - current_time
            wait_time += q[0][1] - current_time
            continue
        # if hq and hq[0][1] > current_time:
        #     current_time += hq[0][1]
        #     continue
        exe = heappop(hq)
        wait_time = current_time - exe[1]    
        current_time += exe[2]
        answer[exe[0]] += wait_time
        wait_time = 0
        complete_pro += 1
    answer[0] = current_time
    return answer


# print(solution([[2, 3, 10], [1, 3, 5], [3, 5, 3], [3, 12, 2]])) # [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
# print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
# print(solution([[1, 0, 1], [2, 0, 1], [3, 0, 1], [4, 0, 1]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
# print(solution([[1, 0, 1], [1, 2, 1], [1, 4, 1], [1, 6, 1]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
# print(solution([[4, 0, 1], [3, 1, 1], [2, 0, 1], [1, 0, 1]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]
print(solution([[1, 0, 1], [2, 2, 2], [3, 4, 2], [4, 8, 2]]))   # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]