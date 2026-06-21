#2026/06/21
#다리를 지나는 트럭
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42583


from collections import deque
def solution(bridge_length, weight, truck_weights):
    q = deque([(truck_weights[0],1)])
    cur = truck_weights[0]
    idx = 1
    t = 1
    while q:
        t += 1
        if t - q[0][1] >= bridge_length:
            w, _ = q.popleft()
            cur -= w
        if idx < len(truck_weights) and cur + truck_weights[idx] <= weight:
            q.append((truck_weights[idx],t))
            cur += truck_weights[idx]
            idx += 1
            
    return t