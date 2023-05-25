'''
문제
어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.

자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.

출력
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.

예제 입력 1 
216
예제 출력 1 
198
'''

import sys
input = sys.stdin.readline
str_N = input().rstrip()
int_N = int(str_N)

min = int_N + 1
check = False
for i in range(int_N):
    sum = i
    for c in str(i):
        sum += int(c)
    if sum == int_N and sum < min:
        min = i
        check = True
        break   # 찾자마자 바로 나가면됨 (최초로 발견된 생성자가 가장 작다고 보장할 수 있음)
if check:
    print(min)
else:
    print(0)


""" 더 빠른 코드
import sys
N=sys.stdin.readline().strip()
L=len(N)
N=int(N)
if N<18: start=0
else: start=N-9*L

for i in range(start, N):
    if N==sum(list(map(int,list(str(i)))),i):
        print(i)
        break
else: print(0)
"""