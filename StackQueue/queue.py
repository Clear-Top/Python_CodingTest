from collections import deque

queue = deque()

queue.append(5) # 5 
queue.append(2) # 5 2 
queue.append(3) # 5 2 3 
queue.append(7) # 5 2 3 7

# 쌓이는 방향이 오른쪽->왼쪽이므로 popleft() 로 선입선출 구현
queue.popleft() # 2 3 7
queue.append(1) # 2 3 7 1 
queue.append(4) # 2 3 7 1 4 
queue.popleft() # 3 7 1 4

# 최상단부터
queue.reverse()
print(queue)

# 최하단부터
queue.reverse()
print(queue)