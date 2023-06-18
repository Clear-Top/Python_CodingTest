'''
1. 각 종목에는 한명만 출전가능
2. 능력치의 합이 최대가 되어야함 (그리디?)
3. 완탐으로 최대가 되는 경로를 탐색하자
    (단, 같은 열에서 선택되면 안된다)
'''

''' 입력정보
ability 행: 각 학생
ability 열: 각 학생의 종목별 능력치
'''

import sys
sys.setrecursionlimit(10**9)
answer = 0
def DFS(visited, ability, depth, sum):
    global answer
    if depth ==len(ability[0]):
        if sum > answer:
            answer = sum
            return
    for i in range(len(ability)):
        max_ability = 0
        max_idx = -1
        for idx,value in enumerate(ability[i]):
            if max_ability < value:
                max_idx = idx
                max_ability = value
        if visited[max_idx] == False:
            visited[max_idx] = True
        DFS(visited, ability, depth+1, sum+max_ability)
    

def solution(ability):
    global answer
    visited_field = [False] * len(ability[0])  
    DFS(visited_field, ability, 0, 0)
    # visited_field:    현재종목에 대표가 뽑혔는지를 확인
    # ability:          학생들의 능력치정보 2차원 배열
    # len(ability[0]):  재귀 깊이는 종목수만 큼만 ex. 3
    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
answer = 0
print(solution([[20, 30], [30, 20], [20, 30]]))