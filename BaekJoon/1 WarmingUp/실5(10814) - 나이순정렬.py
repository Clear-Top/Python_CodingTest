import sys
input = sys.stdin.readline

n = int(input())
results = []

for i in range(n):
    age, name = input().split()
    results.append((int(age), name, i+1))

results.sort(key=lambda x: (x[0], x[2]))

for result in results:
    print(result[0], result[1])


