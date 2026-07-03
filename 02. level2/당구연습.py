#2026/07/03
#당구연습
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/169198


#문제 내용 - 주어진 리스트로 시작점, 벽, 도착점 A - B - C 까지의최소 이동거리 구하기
#balls 는 매회 (start는 동일) 맞춰야하는 target의 위치
#기본 아이디어 -> 모든 대해서 시작점을 대칭이동시켜 직선사이의 거리를 구한다
#문제의 핵심이 다른게 아닌 위 발상을 찾아낸다는 점에서 코딩 능력은 상대적으로 중요하지 않음 -> 그 점에서 level 2인듯
#코딩 구현이 목적이 아니라 수학적 능력을 찾아내는게 목표라면, 코테는 왜 하는 거지? 
#알고리즘을 구현하는 게 아니라 알고리즘 자체를 찾아내길 원한다면, 결국 어디서 본 적 있는 걸 걸러내는 문제 아닌가?
#정말 별로였던 문제

def solution(m, n, startX, startY, balls):
    result = []
    for targetX, targetY in balls:
        walls = [
        ('E',2*m - startX, startY),  # 동쪽벽
        ('W',-startX, startY),        # 서쪽벽
        ('S',startX, -startY),        # 남쪽벽
        ('N',startX, 2*n - startY),   # 북쪽벽
        ]

        leng = float('inf')
        for d, mx, my in walls:
            if d == 'E' and startY == targetY and startX < targetX: continue #예외처리 -> 공이 튕기기전에 타겟에 맞으면 안됨
            if d == 'W' and startY == targetY and startX > targetX: continue
            if d == 'S' and startX == targetX and startY > targetY: continue
            if d == 'N' and startX == targetX and startY < targetY: continue
            leng = min(leng, (mx - targetX)**2 + (my - targetY)**2)
        result.append(leng)
    return result
