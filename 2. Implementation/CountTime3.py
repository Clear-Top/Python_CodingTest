# 완전 탐색 (Brute Forcing)
'''
문제: 주어진 N에 대하여, 00:00:00 ~ N:59:59 까지의 시각 중에서 3이 하나라도 포함되는 모든 경우를 카운팅해보자.
'''

# 시간: 2초
# 메모리: 128MB
# 입력: N (=[0,23])
# 출력: 모든 경우의 수 카운트 결과값

import time

def CountTime3():
    global N
    count = 0
    
    for i in range(N+1):
        if '3' in str(i):
            count += 60 * 60
            continue
        for j in range(60):
            if '3' in str(j):
                count += 60
                continue
            for k in range(60):
                if '3' in str(k):
                    count+=1
    
    return count 

def CountTime3_2():
    global N
    count = 0
    
    for i in range(N+1):
        for j in range(60):
            for k in range(60):
                if '3' in str(i) + str(j) + str(k):
                    count+=1
    
    return count 

N = int(input())
start = time.time()

count = CountTime3()    # 개선 O
count = CountTime3_2()  # 개선 X (naive manner)
print(count)

end = time.time()

print(f"{end-start:.3f} seconds")