# 파이썬의 '리스트' 자료구조는 '스택'과 동일하다

stack = list()

stack.append(5) # 5
stack.append(2) # 5 2
stack.append(3) # 5 2 3
stack.append(7) # 5 2 3 7
stack.pop()     # 5 2 3
stack.append(1) # 5 2 3 1
stack.append(4) # 5 2 3 1 4
stack.pop()     # 5 2 3 1

# 스택의 최상단부터 출력
print(stack[::-1])

# 스택의 최하단부터 출력
print(stack[::1])
