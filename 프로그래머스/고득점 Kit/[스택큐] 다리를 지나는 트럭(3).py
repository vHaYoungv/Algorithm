# 내 풀이
from collections import deque
def solution(bridge_length, weight, truck_weights):
    current_weight = 0
    time = 0
    truck_weights = deque(truck_weights)
    trucks = deque()
    while True:
        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                current_weight += truck_weights[0]
                trucks.append((truck_weights.popleft(), time + bridge_length))
        time += 1
        if trucks and time == trucks[0][1]:
            current_weight -= trucks.popleft()[0]
        if not trucks and not truck_weights:
            return time + 1

# 참고풀이
# [0000] [0007] 이렇게 다리 위의 값을 가시화 하는 방법. 훨씬 직관적이다.
# 리스트를 reverse 해서 pop() 효율을 높이는 방법, 한 쪽으로만 값이 나오는 경우 그냥 stk 인 채로 pop만 사용해도 된다. (굳이 deque X)
from collections import deque

def solution(bridge_length, weight, truck_weights):
    total_weight = 0
    step = 0
    bridge = deque(0 for _ in range(bridge_length))
    truck_weights.reverse()

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        step += 1

    step += bridge_length

    return step
