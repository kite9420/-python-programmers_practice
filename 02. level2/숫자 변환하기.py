#2026/06/03
#숫자 변환하기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/154538

from collections import deque
def solution(x, y, n):
    visited = [False] * (y+1)
    #딕셔너리는 공간이 매우 크고 희소하게 확인 할 때 유리
    #지금의 경우는 리스트를 index를 통해 순회하는 접근하는 것이 해싱 및 리해싱 처리가 없어 더 빠르다
    queue = deque()
    queue.append((x,0))
    visited[x] = True
    
    while queue:
        number, dist = queue.popleft()
        if number == y:
            return dist
        
        for nxt in (number +n, number * 2, number * 3):
            if nxt <= y and not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt,dist +1))
                
    return -1