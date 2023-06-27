import sys

input = sys.stdin.readline

n = int(input())
num = input().strip()

total_sum = sum(map(int, num))

print(total_sum)