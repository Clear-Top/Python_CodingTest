import sys

input = sys.stdin.readline

n = int(input())
point = []

for _ in range(n):
    x,y = map(int, input().strip().split())
    point.append((x,y))

point.sort(key=lambda x:(x[0], x[1]))

for i in range(n):
    print(point[i][0], point[i][1])