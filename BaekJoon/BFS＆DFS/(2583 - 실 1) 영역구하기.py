import sys
from collections import deque
input = sys.stdin.readline

def BFS(tp):
    x, y = tp
    q = deque([(x,y)])
    visited[x][y] = 1
    
    area = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=M or ny<0 or ny >= N:
                continue
            if coordinate[nx][ny] == 0 and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] = 1
                area += 1
    return area

if __name__=="__main__":
    M, N, K = map(int, input().rstrip().split())

    coordinate = [[0] * N for _ in range(M)]

    for k in range(K):
        rec = list(map(int, input().rstrip().split()))
        left_bottom = (M - rec[1] - 1, rec[0])
        right_up = (M - rec[3], rec[2] - 1)
        for i in range(left_bottom[0], right_up[0] - 1, -1):
            for j in range(left_bottom[1], right_up[1] + 1):
                coordinate[i][j] = 1

    # 방문리스트 - 방문O:1, 방문X: 0
    areas = []
    cnt = 0
    visited = [[0] * N for _ in range(M)]
    dx = [-1,+1, 0, 0]
    dy = [0,0,-1,+1]
    for m in range(M):
        for n in range(N):
            if coordinate[m][n] == 0 and visited[m][n] == 0:
                areas.append(BFS((m,n)))
                cnt += 1

    print(cnt)
    print(*sorted(areas))