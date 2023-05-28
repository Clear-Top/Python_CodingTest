import sys
input = sys.stdin.readline

def binary_search(start, end, upper_bound):
    result = 0
    while start<=end:
        mid = (start+end)//2
        temp = 0
        for budget in provinces:
            if budget < mid:
                temp += budget
            else:
                temp += mid
        total = upper_bound - temp
        if total < 0:
            end = mid - 1
        elif total > 0:
            start = mid + 1
            if result <= mid:
                result = mid
        else:
            # 이때는 최적임
            return mid
    return end

if __name__ == "__main__":
    N = int(input())
    provinces = list(map(int, input().split()))
    upper_bound = int(input())

    provinces.sort()

    result = binary_search(0, provinces[-1],upper_bound)

    print(result)