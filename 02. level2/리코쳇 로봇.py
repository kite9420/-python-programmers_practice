#2026/06/5
#리코쳇 로봇
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/169199

#BFS 탐색
from collections import deque

def solution(board):
    m =  len(board) #행
    n = len( board[0]) #열
    dist = [[0] * n for _ in range(m)]
    
    queue = deque()
    #i = 행 j =열
    for i in range(m):
        for j in range(n):
            if board[i][j] == "R":
                queue.append((i,j))
                break
            else:
                continue
            break
    
    dy = 1,-1,0,0
    dx = 0,0,1,-1
    
    while queue:
        # y = 행, x= 열
        y,x= queue.popleft()
        if board[y][x] == "G":
            return dist[y][x]    
    #상하좌우 및 이동조건 -> 헤멘 부분 : while Ture를 사용하지 않고 상하와 좌우를 분리해 따로 While 문을 사용, 동일 위치 중복 방지 및 재방문 조건 추가에 헤맸음
    #                            -> while문 내 탈출조건을 하나로 묶고 정지 조건도 하나로 묶은 후 while문 밖에서 재방문 조건을 추가하여 해결
        for d in range(4):
            ny, nx = y, x
            while True:
                next_y = ny + dy[d]
                next_x = nx + dx[d]
                
                if next_y < 0 or next_y >= m or next_x < 0 or next_x >= n:
                    break
                
                if board[next_y][next_x] == "D":
                    break
                    
                ny, nx = next_y, next_x
            
            if (ny, nx) != (y,x) and dist[ny][nx] == 0:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((ny,nx))
    return -1