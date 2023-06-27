"""
시간초과....?

"""
import sys
input = sys.stdin.readline
n = int(input())
lst = []

for _ in range(n):
    lst.append(int(input()))
lst.sort()
for e in lst:
    print(e)
