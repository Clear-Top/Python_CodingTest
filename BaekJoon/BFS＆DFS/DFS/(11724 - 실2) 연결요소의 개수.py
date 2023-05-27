import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

# 인접리스트로 구현하기
G = [[] for _ in range(N+1)]
for n in range(M):
    n1, n2 = map(int, input().split())
    G[n1].append(n2)
    G[n2].append(n1)

visited = [False] * (N+1)

def DFS(node):
    """
    1. 인접한 정점이 있고, 그 인접정점이 방문하지 않았다면 DFS
    2. DFS 할때마다 cnt+=1
    """
    for adj in G[node]:
        if not visited[adj]:
            visited[adj] = True
            DFS(adj)
    

def BFS(node):
    q = deque([node])
    while q:
        next = q.popleft()
        for adj in G[next]:
            if visited[adj]:
                continue
            q.append(adj)
            visited[adj] = True
    return True

# 인접리스트 - BFS로 구현하기
cnt = 0
for n in range(1,N+1):
    if visited[n]:
        continue
    # BFS(n)
    DFS(n)
    cnt += 1
print(cnt)

# # 인접리스트 - DFS로 구현하기
# cnt = 0
# for n in range(N):
      