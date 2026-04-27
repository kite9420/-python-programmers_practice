#2026/04/26
#연습문제 명예의 전당(1)
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138477
#heap 모듈을 사용하여 코드를 개선하였다
import heapq
def solution(k, score):
    heap = []
    result = []
    for s in score:
        heapq.heappush(heap,s)
        if len(heap) > k:
            heapq.heappop(heap)
        result.append(heap[0])
    return result



'''
def solution(k, score):
    min_score = []
    result = []
    for s in score:
        if len(min_score) < k:
            min_score.append(s)
        elif s > min(min_score):
            min_score.remove(min(min_score))
            min_score.append(s)
        result.append(min(min_score))
    return result
'''