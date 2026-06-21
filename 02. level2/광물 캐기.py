#2026/06/21
#광물 캐기
# #문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172927

from collections import Counter
def solution(picks, minerals):
    result = 0
    cost = [[1,1,1],[5,1,1],[25,5,1]]
    chunks = []
    if len(minerals) > sum(picks) * 5:
        minerals = minerals[:sum(picks) * 5]
    for i in range(0, len(minerals), 5):
        chunks.append(Counter(minerals[i:i+5]))
    chunks.sort(key=lambda c: (c["diamond"], c["iron"]), reverse=True)
    
    idx = 0
    for kind in range(3):
        for _ in range(picks[kind]):
            if idx >= len(chunks):
                break
            c = chunks[idx]
            result += cost[kind][0]*c["diamond"] + cost[kind][1]*c["iron"] + cost[kind][2]*c["stone"]
            idx += 1
    return result