''' 
1. 아이디어 및 알고리즘분류
    - 인출하는 시간이 적은사람들이 앞에 줄서는 것이 가장 좋다.
    - 그리디알고리즘
    
2. 시간복잡도
    - N<1000 이므로, O(N^3)은 안됨
    
3. 예외처리
'''
n = int(input())
people = [ int(x) for x in input().split()]
wait_sum = [0] * n  

people.sort()   # O(nlogn)

# wait_sum[k]: wait_sum[k-1] + people[k]
wait_sum[0] = people[0]
for i in range(1, n):   # O(n)
    wait_sum[i] = wait_sum[i-1] + people[i]

print(sum(wait_sum))    # O(n)
