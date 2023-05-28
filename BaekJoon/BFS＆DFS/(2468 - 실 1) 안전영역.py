'''
예제 입력 1
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

예제 출력 1 
5
'''

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

def BFS(matrix, tp, height):
    x, y = tp
    q = deque([(x,y)])
    matrix[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if matrix[nx][ny] > height and not matrix[nx][ny] == 0:
                q.append((nx,ny))
                matrix[nx][ny] = 0

if __name__ == "__main__":
    N = int(input())

    # Initialize N * N matrix
    G = [list(map(int, input().rstrip().split())) for _ in range(N)]

    # set maximum number of the unflooded houses
    max_unflooded = 0

    # define direction vector of 상 하 좌 우
    dx = [-1, +1 , 0, 0]
    dy = [0, 0, -1, +1]

    # 장마철 1~100 까지의 높이가 상승했을 때를 모두 탐색
    for h in range(1, 10+1):
        temp = 0
        new_matrix = deepcopy(G)
        for i in range(N):
            for j in range(N):
                if new_matrix[i][j] <= h or new_matrix[i][j] == 0:
                    continue
                BFS(new_matrix, (i,j), h)
                temp+=1
        # print(f"높이가 {h} 일 때 안전구역 개수: {temp}")
        # for row in new_matrix:
        #     print(*row)
        if temp > max_unflooded:
            max_unflooded = temp

    print(max_unflooded)