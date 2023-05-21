'''
문제
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 "작은 것을 먼저 방문"하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 "1번부터 N번까지"이다.

입력
첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. "어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다." 입력으로 주어지는 간선은 "양방향(=무방향)" 이다.
4 5 1
1 2
1 3
1 4
2 4
3 4

출력
첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
1 2 4 3
1 2 3 4
'''
import sys
from collections import deque

sys.setrecursionlimit(10**6)

N, M, V = map(int, input().split())

# 인접리스트버전
G = [[] for _ in range(N+1)]

# G.sort(key=lambda x:x[0])
visited = [False] * (N+1)

input = sys.stdin.readline
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

for i in G:
    i.sort()

# print(G)
'''
G = [
    [],
    [2,3,4],
    [1,4],
    [1,4],
    [1,2,3]
]
'''
def DFS(V):
    visited[V] = True
    print(V, end=" ")
    for i in G[V]:
        if visited[i] == False:
            visited[i] = True
            DFS(i)

def BFS(V):
    visited[V] = True
    q = deque([V])

    while q:
        adj_node = q.popleft()
        print(adj_node, end=" ")
        for i in G[adj_node]:
            if visited[i]==False:
                q.append(i)
                visited[i] = True

DFS(V)
print()
visited = [False] * (N+1)
BFS(V)

