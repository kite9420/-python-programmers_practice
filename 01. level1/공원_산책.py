#2026/04/25
#공원 산책
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/172928

#리팩토링 코드 - next 사용 최적화, 방향 벡터 딕셔너리 사용, for, else문 사용 간략화, 불필요한 변수 제거
def solution(park, routes):
    h, w = len(park), len(park[0])
    r,c = next((i,j) for i in range(h) for j in range(w) if park[i][j] == 'S')
    directions = {'N':(-1,0),'S':(1,0),'E':(0,1),'W':(0,-1)}

    for route in routes:
        op, n = route.split()
        n = int(n)
        dr, dc = directions[op]
        nr, nc = r + dr * n, c + dc * n

        if not (0 <= nr < h and 0 <= nc < w):
            continue
        for step in range(1, n + 1):
            if park[r + dr * step][c + dc * step] == 'X':
                break
        else:
            r,c = nr, nc
    return [r, c]




'''
초기코드
def solution(park, routes):
    position = []
    next_position = []
    obstacles = []
    h = len(park)
    w = len(park[0])
    for i in range(h):
        for j in range(w):
            if park[i][j] == "S":
                position = [i,j]
            if park[i][j] == "X":
                obstacles.append([i,j])
    
    for route in routes:
        route = route.split()
        if route[0] == 'N':
            next_position = [position[0]-int(route[1]),position[1]]
        elif route[0] == 'S':
            next_position = [position[0]+int(route[1]),position[1]]
        elif route[0] == 'E':
            next_position = [position[0],position[1]+int(route[1])]
        elif route[0] == 'W':
            next_position = [position[0],position[1]-int(route[1])]
        if 0 <=next_position[0] <= h-1 and 0<= next_position[1] <= w-1:
            stop = False
            for i in range(min(position[0],next_position[0]),max(position[0],next_position[0])+1):
                if stop:
                    break
                for j in range(min(position[1],next_position[1]),max(position[1],next_position[1])+1):
                    if [i,j] not in obstacles:
                        pass
                    else:
                        stop = True
                        break
            if not stop:
                position = next_position
    return position
'''