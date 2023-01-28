'''
BFS 의의: 시작노드에서 부터 가장 가까운 순서대로 방문한다.
'''

import time
from collections import deque

# DFS 와는 다르게 BFS는 큐(deque) 자료구조를 활용하여 반복문으로 해결한다. 
def bfs(graph, start, visited):
    # 리스트 [start(=1)] 을 원소로 갖는 큐 생성
    # 즉, 시작노드 1을 가장 먼저 큐에 넣고 시작
    queue = deque([start]) 
    visited [start] = start
    
    while queue:    # 큐(queue)에 원소가 존재하는한 반복
        processedNode = queue.popleft()
        print(processedNode, end=' ')
        for i in graph[processedNode]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
    

# [2차원 리스트]를 사용한 그래프표현
graph =[
    [],         # 일반적으로, 그래프문제에서는 노드가 1번부터 시작하므로, 직관적인 처리를 위해 0번노드를 비어있는 리스트로 사용
    [2,3,8],    # 1번노드와 연결된 노드들: 2, 3, 8
    [1,7],      # 2번노드와 연결된 노드들: 1, 7
    [1,4,5],    # 3번노드와 연결된 노드들: 1, 4, 5
    [3,5],      # 4번노드와 연결된 노드들: 3, 5
    [3,4],      # 5번노드와 연결된 노드들: 
    [7],        # 6번노드와 연결된 노드들: 7
    [2,6,8],    # 7번노드와 연결된 노드들: 2, 6, 8
    [1,7]       # 8번노드와 연결된 노드들: 1, 7
] 

start = time.time()

# 모든 노드는 방문되지 않았다고 가정
# 9개의 false 아이템을 갖는 리스트 초기화
visited = [False] * 9  

bfs(graph, 1, visited)       # 시작노드: 1

end = time.time()
print(f"\n{end-start:.5f} seconds")