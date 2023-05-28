import sys
from collections import deque
input = sys.stdin.readline

def BFS(tp):
    x, y = tp
    q = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if complexes[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                cnt += 1
    return cnt

if __name__ == "__main__":
    N = int(input())

    # 동네지도 초기화
    complexes = [list(map(int, input().rstrip())) for _ in range(N)]

    # 각 단지의 아파트 수
    sizeOfComplexes = list()

    # Direction vector
    dx = [-1, +1, 0, 0]
    dy = [0, 0, -1, +1]
    visited = [[0]*N for _ in range(N)]
    numOfComplexes = 0 
    for i in range(N):
        for j in range(N):
            if complexes[i][j] == 1 and visited[i][j] == 0:
                sizeOfComplexes.append(BFS((i,j)))
                numOfComplexes += 1     

    sizeOfComplexes.sort()
    print(numOfComplexes)
    for i in sizeOfComplexes:
        print(i)
            
# for row in complexes:
#     print("".join(map(lambda i: str(i), row)))