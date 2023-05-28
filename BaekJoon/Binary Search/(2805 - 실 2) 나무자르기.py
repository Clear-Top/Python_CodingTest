import sys
from bisect import bisect_left
input = sys.stdin.readline

def binary_search(start, end, trees):
    while start<=end :    
        mid = (end + start) // 2    # 가운데 나무길이 (실제하는 나무인지는 관심없음)
        total_sum = 0
        for tree in trees:
            if tree > mid:
                total_sum += (tree-mid)
        if target < total_sum:    # height 가 너무 낮다
            start = mid + 1
        elif target > total_sum:  # height 가 너무 높다
            end = mid - 1
        else:
            return mid
    return end

if __name__ == "__main__":
    N, target = map(int, input().rstrip().split())
    trees = [int(tree) for tree in input().rstrip().split()]

    # 나무들 팀소트 정렬
    trees.sort() # O(NlogN)

    print(binary_search(0, trees[-1], trees))

