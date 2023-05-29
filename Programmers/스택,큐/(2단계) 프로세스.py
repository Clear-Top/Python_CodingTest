''' 아이디어:
1. 원하는 프로세스의 실행순서는 location이 된다.
2. 앞쪽에 있는걸 계속 팝하고 자신보다 우선순위 높은 것이 있는지 탐색
    - pop 할때마다 실행순서 += 1
'''
from collections import deque

def solution(priorities, location):
    exe_time = 0
    my_process_location = location
    q = deque(priorities)
    
    while True:
        flag = True
        cur_process = q.popleft()
        my_process_location -= 1
        for other_process in q:
            if other_process > cur_process:
                flag = False
                break
        if flag == False:
            if my_process_location < 0:
                my_process_location = len(q)
            q.append(cur_process)
            continue
        exe_time += 1
        if my_process_location < 0:
            return exe_time
        

if __name__=="__main__":
    print(solution([1,1,9,1,1,1],0))