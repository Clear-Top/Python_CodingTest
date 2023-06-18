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

field = ['테니스','탁구','수영']

def DFS(visited_stu, visited_field, ability, depth, sum):
    global answer
    if depth ==len(ability[0]):
        if sum > answer:
            answer = sum
            return None
    for i in range(len(ability)):
        if visited_stu[i] == True:
            continue 
        visited_stu[i] = True
        max_ability = 0
        max_idx = -1
        for idx,value in enumerate(ability[i]):
            if visited_field[idx] == True:
                continue
            if max_ability < value:
                max_ability = value
                max_idx = idx
        visited_field[max_idx] = True
        # print(f"학생{i} 은 {field[max_idx]} 의 대표로 선출되었습니다.")
        DFS(visited_stu, visited_field, ability, depth+1, sum + max_ability)
        visited_field[max_idx] = False
        visited_stu[i] = False
    

def solution(ability):
    global answer
    visited_field = [False] * len(ability[0])  
    visited_stu = [False] * len(ability)
    depth = 0
    max_sum = 0
    DFS(visited_stu, visited_field, ability, depth, max_sum)
    # visited_field:    현재종목에 대표가 뽑혔는지를 확인
    # ability:          학생들의 능력치정보 2차원 배열
    # len(ability[0]):  재귀 깊이는 종목수만 큼만 ex. 3
    return answer

answer = 0
print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))
answer = 0
print(solution([[20, 30], [30, 20], [20, 30]]))