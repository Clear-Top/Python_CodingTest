import sys
input = sys.stdin.readline
# INF = 10**9

# 정점개수
N = int(input())

# 입력받기
matrix = []
for n in range(N):
    matrix.append(list(map(int, input().rstrip().split())))

def Floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if matrix[i][k]==1 and matrix[k][j] ==1:
                    matrix[i][j] = 1
            
Floyd()
for row in matrix:
    print(" ".join(map(str, row)))

  
