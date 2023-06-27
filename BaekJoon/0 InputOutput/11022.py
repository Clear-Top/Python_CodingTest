import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    a1, a2 = map(int, input().split())
    print(f"Case #{i+1}:",a1,'+',a2,'=',a1+a2)