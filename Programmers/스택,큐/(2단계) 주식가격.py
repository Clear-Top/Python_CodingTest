'''
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.  => "O(NlogN)"

입출력 예
prices      	return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
'''

def solution(prices):
    """
    1. 시간 요구사항: O(N^2) 은 피해야만 한다.
    2. 아이디어:
        - prices를 스택으로
        - prices 에서 pop할때마다 cnt += 1
        - 가장 최근에 pop한것이 이전에 pop한것보다 크다면 pop한 개수만큼 시간기록
        - 
    3. 변수설명
        - prices: 주식가격 리스트
        - times: 시간기록 정보

    """
    times = [ 0 for _ in prices ]

    cnt = 0
    index = 0
    previous_price = 0
    while prices:
        price = prices.pop()
        if price > previous_price:
            cnt = 1
        times[-1-index] = cnt
        cnt += 1
        index += 1
        previous_price = price
    return times

print(solution([1,2,3,2,3]))