'''
문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''

'''
1. N과 M을 서로 비교하는 것
2. 출력은 M을 기준으로 줄바꿈 비트형식으로
3. N 은 정렬 => NlogN = 100,000 X log(100,000) = 100,000 X 약 17 = 1700,000 (170만); M개를 이진탐색 MlogN = 170만
    => 토탈 340만 ... 1초안에 해결가능
'''

import sys
input = sys.stdin.readline

N = int(input().strip())
list_N = list(map(int, input().split()))
list_N.sort()

M = int(input().strip())
list_M = list(map(int, input().split()))

check_M = [0] * M

for index, m in enumerate(list_M):
    start = 0
    end = N - 1
    while start<=end:
        mid = (start + end) //2
        if list_N[mid] == m:
            check_M[index] = 1
            break
        elif list_N[mid] > m:
            end = mid - 1
        else:   # list_N[mid] < m
            start = mid + 1

for m in check_M:
    print(m)