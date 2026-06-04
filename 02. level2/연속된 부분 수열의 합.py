#2026/06/03
#연속된 부분 수열 합의 개수 
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    n = len(sequence)
    # 문제의 조건에서 우측으로 한칸 가면 합은 무조건 증가, 좌측으로 한칸 당기면 합은 무조건 감소
    #윈도우 슬라이드 방식으로 해결
    left = 0
    total = 0
    best = None
    
    for right in range(n):
        total += sequence[right]
        while total > k:
            total -= sequence[left]
            left += 1
        if total == k:
            length = right - left +1
            if best is None or length < best[0]:
                best = (length, left, right)
    return [best[1],best[2]]