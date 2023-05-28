'''
문제
전쟁은 어느덧 전면전이 시작되었다. 결국 전투는 난전이 되었고, 우리 병사와 적국 병사가 섞여 싸우게 되었다. 그러나 당신의 병사들은 흰색 옷을 입고, 적국의 병사들은 파란색 옷을 입었기 때문에 서로가 적인지 아군인지는 구분할 수 있다. 문제는 같은 팀의 병사들은 모이면 모일수록 강해진다는 사실이다.
N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다. 과연 지금 난전의 상황에서는 누가 승리할 것인가? 단, 같은 팀의 병사들이 대각선으로만 인접한 경우는 뭉쳐 있다고 보지 않는다.

입력
첫째 줄에는 전쟁터의 가로 크기 N, 세로 크기 M(1 ≤ N, M ≤ 100)이 주어진다. 그 다음 두 번째 줄에서 M+1번째 줄에는 각각 (X, Y)에 있는 병사들의 옷색이 띄어쓰기 없이 주어진다. 모든 자리에는 병사가 한 명 있다. B는 파란색, W는 흰색이다. 당신의 병사와 적국의 병사는 한 명 이상 존재한다.

출력
첫 번째 줄에 당신의 병사의 위력의 합과 적국의 병사의 위력의 합을 출력한다.
'''
import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())

G = []
for _ in range (M):
    n = list(input().strip())
    G.append(n)

# print(G)

# 방향벡터정의 (우, 좌, 아래, 위)
dx = [0,0,+1,-1]
dy = [+1,-1,0,0]

def BFS_W(start):
    warrior = 1
    x, y = start
    q = deque([(x,y)])
    G[x][y] = "X"     # 방문체크

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            if G[nx][ny] == "W":
                q.append((nx, ny))
                warrior += 1
                G[nx][ny] = "X"
    return warrior

def BFS_B(start):
    warrior = 1
    x, y = start
    q = deque([(x,y)])
    G[x][y] = "X"     # 방문체크

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > M-1 or ny < 0 or ny > N-1:
                continue
            if G[nx][ny] == "B":
                q.append((nx, ny))
                warrior += 1
                G[nx][ny] = "X"
    return warrior


# (0,0)~(m,n): 완전탐색
power_of_W = 0
power_of_B = 0
for m in range(M):
    for n in range(N):
        if G[m][n] == 'W':
            power_of_W += (BFS_W((m,n))**2)
        elif G[m][n] == 'B':
            power_of_B += (BFS_B((m,n))**2)

print(power_of_W, power_of_B)
