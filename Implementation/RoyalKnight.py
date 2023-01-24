'''
문제: 체스판의 나이트(말)를 옮길 때 이동가능한 경우의 수를 카운팅한다.
    나이트는 이동할때 아래를 따른다.
    1. 수평으로 두 칸 -> 수직으로 한 칸
    2. 수직으로 두 칸 -> 수평으로 한 칸
    3. 행(Row)은 '1~8'로 표현되고, 열(Column)은 'a~h' 로 표현된다.
    4. 체스판 밖으로 이동할 수 없다.
'''

# 시간: 1초
# 메모리: 128MB
# 입력: 현재 나이트 위치 ex. a1 (a열 1번째)
# 출력: 현재 위치에서 나이트가 이동할 수 있는 경우의 수

import time

def royalKnight():
    count = 0
    hor = [2,-2,1,-1]    # 수평이동
    ver = [1,-1,2,-2]    # 수직이동
    current_hor = ord(current_posit[0])
    current_ver = int(current_posit[1])
    
    # print(current_hor)
    # print(current_ver)
    
    '''
    가능한 경우의 수
    hor     ver
    0       0       # → → ↑
    0       1       # → → ↓
    1       0       # ← ← ↑
    1       1       # ← ← ↓
    2       2       # → ↑ ↑
    2       3       # → ↓ ↓
    3       2       # ← ↑ ↑
    3       3       # ← ↓ ↓
    '''
    
    for i in range(4):
        after_hor = current_hor + hor[i]
        for j in range(4):
            if (i==0 or i==1) and (j==2 or j==3):
                continue
            if (i==2 or i==3) and (j==0 or j==1):
                continue
            after_ver = current_ver + ver[j]
            if ('a'<= chr(after_hor) <= 'h') and (1 <= after_ver <= 8):
                count+=1
                
    return count

current_posit = input()

start = time.time()

count = royalKnight()
print(count)

end = time.time()

print(f"{end-start:.3f} seconds")