import heapq

"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
"""

def solution(scoville, K):
    num_mix = 0
    heapq.heapify(scoville) # O(N)

    while scoville[0] < K :
        try:
            current_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
            heapq.heappush(scoville,current_scoville)
            num_mix += 1
        except:
            return -1

    return num_mix

print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 1, 1, 1, 1, 1], 7))
print(solution([1, 1, 1, 1], 7))
print(solution([1, 2, 9, 10, 12], 7))