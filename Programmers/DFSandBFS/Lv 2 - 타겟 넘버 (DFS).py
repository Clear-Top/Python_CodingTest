import sys
sys.setrecursionlimit(10**9)
answer = 0

def DFS(numbers, current_idx, target, depth, sum):
    global answer
    if depth == len(numbers):
        if sum == target:
            answer += 1
            return
        else:
            return
    else:   # sum!=target or number가 비어있지 않다면s
        DFS(numbers, current_idx+1, target, depth+1, sum+numbers[current_idx])
        DFS(numbers, current_idx+1, target, depth+1, sum-numbers[current_idx])
    return answer

def solution(numbers, target):
    global answer
    current_idx = 0     # numbers[0]
    depth = 0
    sum = 0
    DFS(numbers, current_idx, target, depth, sum)

    return answer

print(solution([1, 1, 1, 1, 1], 3)) # 5
answer=0
print(solution([4,1,2,1], 4)) # 2