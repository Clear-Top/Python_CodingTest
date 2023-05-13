def solution(arr, k):
    answer = [k*i for i in arr if k%2==1]
    return answer

arr = [1, 2, 3, 100, 99, 98]

result = solution(arr, 3)
# result = solution(arr, 2)

print(result)