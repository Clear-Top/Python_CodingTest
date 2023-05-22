'''
문제
서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?

입력
첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

출력
첫째 줄에 자연수 N의 최댓값을 출력한다.

예제 입력 
200
예제 출력 
19
'''

'''
key: 최대한 여러번 더해서 S를 만들어야 함
1. 작은수부터(1~) S보다 커지는 순간까지 더함
2. 합이 S보다 커지면 탈출
3. (key) S=1 이면 cnt=1, S=2 이면 cnt=1
'''

import sys
input = sys.stdin.readline

S = int(input())

sum = 0
cnt = 0
for i in range(1,S+1):
    # print(f"{sum}+{i}={sum+i}")
    sum += i
    cnt += 1
    if (sum>S):
        cnt-=1
        break
print(cnt)