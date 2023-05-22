'''
문제
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 'N개'를 가지고 있다. '정수 M'개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 상근이가 가지고 있는 숫자 카드의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다. 숫자 카드에 적혀있는 수는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다. 두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
셋째 줄에는 M(1 ≤ M ≤ 500,000)이 주어진다. 넷째 줄에는 상근이가 가지고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며, 이 수는 공백으로 구분되어져 있다. 이 수도 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다

출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.
'''

'''
1. 상근이의 N개의 숫자카드에 M개의 정수중에 가지고있는것과 없는것 판별하기 (완전탐색)
2. 브루트포스 할 때 하나하나 대조하면 N*M=50만X50만=25,000,000 
3. M크기의 리스트에 2bit로 표현
'''
import sys
input = sys.stdin.readline

N = int(input())
list_N = list(input().split())
M = int(input())
list_M = list(input().split())

# exist = [0] * M
list_N.sort()

for target in list_M:
    start = 0
    end = N - 1
    flag = False
    while start<=end:
        mid = (start+end)//2
        if list_N[mid] == target:
            flag = True
            break
        elif list_N[mid] < target:
            start = mid + 1
        else: # list_N[mid] > target
            end = mid - 1
    if flag == False:
        print("0", end=" ")
    else:
        print("1", end=" ")
        
''' 문제발생
3초로 시간초과 발생
why?
- 정렬: O(NlogN)
- N크기의 리스트를 M번 이분탐색: MNlogN 
=> 2500만... 이러면 시간초과임
'''