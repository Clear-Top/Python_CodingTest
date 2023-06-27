import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a1, a2 = map(int, input().split(','))
    print(a1+a2)