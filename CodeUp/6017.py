import sys

input = sys.stdin.readline

s = input().strip()

result = ''
for _ in range(3):
    result += s
    result += ' '

print(result)