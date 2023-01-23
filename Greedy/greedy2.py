'''
어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 수행
1. N에서 1을 빼기
2. N을 K로 나누기

N과 K가 주어질 때 N이 1이 될 때까지 1번 혹은 2번의 과정을 수행해야 하는 최소횟수는?
'''
# 풀이시간: 15분
# 시간: 2초
# 메모리 제한: 128MB
# N = [1, 100,000] ** O(NlogN)
# K = [2, 100,000]

import time

def greedy2(N, K):
    global count
    while True:
        target = (N//K) * K
        count += (N-target)
        if N<K:
            count += (N-1)
            break
        N //= K
        count+=1

N, K = map(int,input().split())
count = 0

start = time.time()

greedy2(N, K)
print(count)

end = time.time()

print(f'{end-start:.10f}')
