# from collections import deque
import heapq
def solution(operations):
    min_h = []
    max_h = []
    for operation in operations:
        element = operation.split(' ')
        if element[0] == 'I':   # 삽입
            heapq.heappush(min_h, int(element[1]))
            heapq.heappush(max_h, -int(element[1]))
        elif element[0] == 'D': # 삭제
            if element[1] == 1: # 최댓값삭제
                print(f"{heapq.heappop(max_h)} 이 삭제되었습니다.")
            else: # element[1] == -1 # 최솟값삭제
                print(f"{heapq.heappop(min_h)} 이 삭제되었습니다.")
    
    print(min_h)
    print(max_h)
    # return answer

solution(["I -45", "I 653", "I 1", "I -642", "I 45", "I 97", "I 1", "I -1", "I 333"])
# solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
# solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])

