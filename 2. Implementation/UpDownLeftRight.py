'''
문제: N x N 정사각형이 주어져있으며 (N>=1), 이 공간은 1 x 1의 작은 정사각형으로 이루어져있다.
    이때, 이 공간에서의 위치좌표는 다음과 같이 정의된다.
        - 가장왼쪽 위: (1,1)
        - 가장오른쪽 아래: (N,N)
    이동을 위한 키워드는 아래와 같이 정의된다.
        - U: 위로 한 칸
        - D: 아래로 한 칸
        - L: 왼쪽으로 한 칸
        - R: 오른쪽으로 한 칸
    단, 위치 이동중에 주어진 공간을 벗어난다면, 해당 키워드는 무시된다.
    단, x축은 row, y축은 column 을 의미한다.
'''

# 시간: 2초
# 메모리:128 MB
# 입력 1: N (범위: 1~100)
# 입력 2: 이동키워드 (개수: 1~100)

import time

def UpDownLeftRight():
    global N
    move_types = ['U', 'D', 'L', 'R']

    # Up:       drow[0], dcolumn[0]
    # Down:     drow[1], dcolumn[1]
    # Left:     drow[2], dcolumn[2]
    # Right:    drow[3], dcolumn[3]
    drow = [-1,1,0,0]       # x
    dcolumn = [0,0,-1,1]    # y
    current_index = [1,1]

    for move in moves:
        # 이동이 무효되는 경우
        '''
        Case 1: current_index[1,-] 인데, Up
        Case 2: current_index[-,1] 인데, Left
        Case 3: current_index[N,-] 인데, Down
        Case 4: current_index[-,N] 인데, Right
        '''
        # 이동이 무효되지 않는 경우, 이동 수행
        for index in range(0, len(move_types)):
            if move == move_types[index]:
                if current_index[0] == 1 and move=='U':
                    continue
                elif current_index[1] == 1 and move=='L':
                    continue
                elif current_index[0] == N and move=='D':
                    continue
                elif current_index[1] == N and move=='R':
                    continue
                current_index[0] += drow[index]
                current_index[1] += dcolumn[index]

    # print(current_index[0],current_index[1])
    return current_index[0], current_index[1]


N = int(input())
moves = input().split()

start = time.time()

x, y = UpDownLeftRight()
print(x, y)

end = time.time()

print(f"{end-start:.3f} seconds")