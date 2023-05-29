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
    
    # 대기트럭에 대한 큐
    q_truck = deque(truck_weights)
    # 다리를 지나가는 트럭
    q_bridge = deque([0 for _ in range(bridge_length)])
    # 경과시간
    time = 0
    # 현재다리 위의 무게
    current_weight = 0
    while q_truck or current_weight > 0: 
        if q_truck:
            truck = q_truck[0]
        old_truck = q_bridge.popleft()
        current_weight -= old_truck
        if current_weight + truck <= weight and q_truck:
            q_bridge.append(q_truck.popleft())
            current_weight += truck
        else:
            q_bridge.append(0)
        time += 1
    return time

print(solution(100,100,[10]))