#2026/05/21
#연속된 부분 수열 합의 개수 
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131701

#  연산양을 줄이기 위해 슬라이딩 윈도우를 사용. 
def solution(elements):
    sum_elements = set()
    n = len(elements)
    for w in range(1, n + 1):
        total = sum(elements[j] for j in range(w))
        sum_elements.add(total)
        for i in range(1, n):
            total = total - elements[(i - 1) % n] + elements[(i - 1 + w) % n]
            sum_elements.add(total)
    return len(sum_elements)
