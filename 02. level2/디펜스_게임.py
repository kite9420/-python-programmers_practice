#2026/06/24
#디펜스 게임
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/142085
#min heap을 뒤집어서 max heap으로 사용하는게 핵심이었던 문제

#문제의 내용을 sum(enemy[:x]) <= n이 되게 하는 x를 찾는걸로 생각. k만큼 숫자를 뺄 수 있음
#enemy의 숫자를 더해간다. 더하다가 n보다 커지면 enemy 중 가장 큰수를 제거한다.

import heapq
def solution(n, k, enemy):
    heap = []
    total = 0
    count = 0
    for i in enemy:
        total += i
        heapq.heappush(heap,-i)
        if total > n:
            if k:
                l = heapq.heappop(heap)
                k -= 1
                total += l
            else:
                return count
        count += 1
    return count