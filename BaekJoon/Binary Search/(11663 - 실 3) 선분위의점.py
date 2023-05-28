from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline
            
if __name__=="__main__":
    # N: 점개수, M: 선분개수
    N, M = map(int, input().split())

    points = [int(x) for x in input().split()]
    points.sort()

    temp = []
    for _ in range(M):
        temp.append(tuple(map(int, input().split())))

    for t in temp:
        left = bisect_left(points, t[0])
        right = bisect_right(points, t[1])
        print(right-left)