import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    for _ in range(i+1):
        print('*',end="")
    print()