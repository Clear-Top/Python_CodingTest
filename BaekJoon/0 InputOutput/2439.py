# import sys

# input = sys.stdin.readline

# n = int(input())

# for i in range(n):
#     for j in range(n-i-1):
#         print(' ',end="")
#     for k in range(i+1):
#         print('*',end="")
#     print()

n = int(input())

for i in range(n):
    print(('*'*(i+1)).rjust(n, ' '))