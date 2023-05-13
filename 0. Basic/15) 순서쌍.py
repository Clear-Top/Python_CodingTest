'''
시간초과남
'''
# from itertools import product
# def solution(n=10):
#     pairs = list(product(range(1,n+1),repeat=2))
#     cnt=0
#     for pair in pairs:
#         if n == pair[0]*pair[1]:
#             cnt+=1
#     return cnt
# print(solution(100))

'''
N 범위에 따른, 시간복잡도 설계 (보통 1초에 2,000만~1억)
1. N<=500       : O(N^3)
2. N<=2,000     : O(N^2)
3. N<=100,000   : O(NlogN)
4. N<=10,000,000: O(N)

n <= 1,000,000 시간복잡도는 O(NlogN) ~ O(N) 이어야 한다. 
'''
def solution(n=100):
    var = list(filter(lambda x:n%x==0, range(1,n+1)))
    return len(var)
print(solution())