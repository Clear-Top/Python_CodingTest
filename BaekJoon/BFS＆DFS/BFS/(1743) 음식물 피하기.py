'''
문제
코레스코 콘도미니엄 8층은 학생들이 3끼의 식사를 해결하는 공간이다. 그러나 몇몇 비양심적인 학생들의 만행으로 음식물이 통로 중간 중간에 떨어져 있다. 이러한 음식물들은 근처에 있는 것끼리 뭉치게 돼서 큰 음식물 쓰레기가 된다. 
이 문제를 출제한 선생님은 개인적으로 이러한 음식물을 실내화에 묻히는 것을 정말 진정으로 싫어한다. 참고로 우리가 구해야 할 답은 이 문제를 낸 조교를 맞추는 것이 아니다. 
통로에 떨어진 음식물을 피해가기란 쉬운 일이 아니다. 따라서 선생님은 떨어진 음식물 중에 제일 큰 음식물만은 피해 가려고 한다. 
선생님을 도와 제일 큰 음식물의 크기를 구해서 “10ra"를 외치지 않게 도와주자.

입력
첫째 줄에 통로의 세로 길이 N(1 ≤ N ≤ 100)과 가로 길이 M(1 ≤ M ≤ 100) 그리고 음식물 쓰레기의 개수 K(1 ≤ K ≤ N×M)이 주어진다.  그리고 다음 K개의 줄에 음식물이 떨어진 좌표 (r, c)가 주어진다.
좌표 (r, c)의 r은 위에서부터, c는 왼쪽에서부터가 기준이다. 입력으로 주어지는 좌표는 중복되지 않는다.

출력
첫째 줄에 음식물 중 가장 큰 음식물의 크기를 출력하라.
'''

''' 아이디어
BFS 로 만들어 질 수 있는 덩어리 중에서 가장 큰 덩어리의 크기 구하기
'''
import sys
from collections import deque
input = sys.stdin.readline
# N: 행, M: 열
N, M, K = map(int, input().split())

G = [[0]* M for _ in range(N)]
for i in range(K):
    n, m = map(int, input().split())
    G[n-1][m-1] = 1
# print(G)

# 오 왼 아 위
dx = [0, 0, +1, -1]
dy = [+1, -1, 0, 0]

def BFS(x, y):   # parameter: 좌표
    q = deque([(x,y)])
    G[x][y] = 0
    size = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:
                continue
            if G[nx][ny] == 1:
                q.append((nx,ny))
                G[nx][ny] = 0
                size += 1
    return size

max = 0
size_of_trash = 0
for n in range(N):
    for m in range(M):
    # for j in G[i]:
        if G[n][m] == 1:
            size_of_trash = BFS(n, m) 
        if max < size_of_trash:
            max = size_of_trash
print(max)