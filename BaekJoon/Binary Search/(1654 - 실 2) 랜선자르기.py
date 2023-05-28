import sys
input = sys.stdin.readline

def binary_search(start, end, target):
    max_length = 0
    while start<=end:
        mid = (start+end)//2
        cnt = 0
        for l in lan:
            cnt += (l//mid)
        if cnt < target:
            end = mid - 1
        elif cnt > target:
            if max_length < mid:
                max_length = mid
            start = mid + 1
        else:
            if max_length < mid:
                max_length = mid
            start = mid + 1
            # return max_length
    return max_length

if __name__ == "__main__":
    K, N = map(int, input().split())
    
    lan = [ int(input().rstrip()) for _ in range(K)]

    lan.sort()

    print(binary_search(1, lan[-1], N))
    