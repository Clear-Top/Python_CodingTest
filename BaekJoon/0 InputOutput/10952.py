import sys

input = sys.stdin.readline

a1, a2 = map(int, input().split())
while (not a1 is 0) and (not a2 is 0):
    print(a1+a2)
    a1, a2 = map(int, input().split())