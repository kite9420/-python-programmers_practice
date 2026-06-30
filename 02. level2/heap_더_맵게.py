#2026/06/30
#더 맵게
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42626
#너무 쉬웠던 문제라 다른 설명은 없음

import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    count = 0
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2*second)
        count += 1
    return count