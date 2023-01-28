'''
그래프를 DFS 방식으로 순회하기
    - 시작노드는 미리 주어진다.
    - 각 노드에서 다음 노드를 방문할때, 낮은 숫자가 기록된 노드를 먼저 방문한다.
'''
import time

def dfs (graph, current_node, visited):
    print(current_node, end=' ')
    
    visited[current_node] = True
    for i in graph[current_node]:
        if visited[i]==False:
            dfs(graph, i, visited)
    return 
    


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

# 모든 노드는 방문되지 않았다고 가정
visited = [False] * 9  # 9개의 false 아이템을 갖는 리스트 초기화

start = time.time()

dfs(graph, 1, visited)       # 시작노드: 1

end = time.time()
print(f"\n{end-start:.5f} seconds")
