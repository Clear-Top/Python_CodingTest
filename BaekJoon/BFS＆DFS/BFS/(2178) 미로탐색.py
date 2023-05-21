'''
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
'''

'''
1. (0,0)부터 탐색시작
2. 최단거리 구하는 거니까, BFS로 작성하기
3. 매 칸마다 +1 씩 업데이트해주면 됨
'''
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) 
G = []

for i in range (N):
    before = list(input().rstrip())
    G.append(list(map(int, before)))

# for x in G:
#     print(x)
# print()

# 방향벡터 정의 (오, 왼, 아, 위)
dx = [0, 0, +1,-1]
dy = [+1, -1, 0, 0]
def BFS():
    q = deque([(0,0)])  # (1,1)은 반드시 1이라고 가정해야함
    while q:
        x, y = q.popleft()
        for i,j in zip(dx,dy):
            nx = x + i
            ny = y + j
            if nx < 0 or nx > N-1 or ny < 0 or ny > M-1:
                continue
            if G[nx][ny] == 1:   # 방문한 적이 없다면
                 G[nx][ny] += G[x][y]
                 q.append((nx,ny))
    return 

BFS()
print(G[N-1][M-1])