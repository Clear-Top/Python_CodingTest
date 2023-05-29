from collections import deque

def bridge_and_truck(b,t):
    print(f"다리상태: {b}")
    print(f"트럭대기열: {t}")
    print()

def solution(bridge_length: int, weight: int, truck_weights: list):
    """
    1. 문제이해:
        - 트럭한대가 다리를 건너는데에 걸리는 시간: 1초
        - 먼저 다리를 건너고있던 트럭이 다리를 지난다. (즉, 같이 다리를 건너더라도 한꺼번에 도착하는 경우는 없다.)
    
    2. 시간복잡도 및 자료구조:
        - 자료구조: 큐
        - 시간복잡도: 처리할 트럭은 최대 10,000대 이므로 O(N^2) ~ O(NlogN)
        
    3. 아이디어:
        1) 앞에서부터 큐에 삽입, 삽입때마다 시간 += 1
        단, 중량초과시 append해서는 안됨 & 큐의 사이즈가 bridge_length 를 초과하면 안됨
        2) pop할때 마다 시간 += 1
        3) 종료조건: 다리에 대한 큐가 비면 종료
    """
    
    # print(bridge_length, weight, truck_weights)
    
    spend_time = 0
    
    q_for_truct = deque(truck_weights)
    q_for_bridge = deque()
    weight_on_bridge = 0
    length_of_bridge = 0
    
    while q_for_truct:
        
        bridge_and_truck(q_for_bridge,q_for_truct)  # 디버깅
        truck = q_for_truct[0]
        
        # 트럭이 다리에 올라갔을때 가정
        weight_on_bridge += truck
        length_of_bridge += 1
        # spend_time += 1
        
        if length_of_bridge < bridge_length and weight_on_bridge < weight:
            if q_for_bridge:
                truck2 = q_for_bridge.popleft()
                weight_on_bridge -= truck2
                length_of_bridge -= 1
            truck = q_for_truct.popleft()
            q_for_bridge.append(truck)
        else:   # 제한사항을 둘 중 하나라도 만족못했을 때 
            if q_for_bridge:
                truck2 = q_for_bridge.popleft()
                weight_on_bridge -= truck2
                length_of_bridge -= 1
            weight_on_bridge -= truck
            length_of_bridge -= 1
            # spend_time += 1
        spend_time += 1
    print(spend_time)

solution(2,10,[7,4,5,6])