#2026/07/06
#2023 KAKAO 택배 배달과 수거하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150369

# 거리 1짜리 각 구간을 몇번 왕복하느냐를 세는게 빠르다는걸 찾아내기까지 너무 어려웠던 문제.
# 반복문 구조를 어떻게 짜야할지, 한 집에 방문했을 때 남는 capacity를 이전에 어떻게 전달해야할지 구조적으로 풀 수 없었으나 다른 접근을 떠올리고 해결됨
# 문제가 너무 어렵거나 풀리지 않으면 문제를 쉽게 풀 수 있는 알고리즘을 찾기.

def solution(cap, n, deliveries, pickups):
    dist = 0
    d_sum = 0
    p_sum = 0
    d = 0
    p = 0
    for i in range(n-1, -1, -1):
        d_sum += deliveries[i]
        p_sum += pickups[i]
        while d * cap < d_sum:
            d += 1
        while p * cap < p_sum:
            p += 1
        if d > p:
            dist += d * 2
        else:
            dist += p * 2
    return dist

