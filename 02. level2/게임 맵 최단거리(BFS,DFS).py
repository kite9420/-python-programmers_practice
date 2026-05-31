#2026/05/31
#게임 맵 최단거리
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1844

#BFS
#너비 우선 탐색으로 동심원처럼 퍼져나가며 탐색

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dist = [[0] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 1

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return dist[x][y]

# 상하좌우 이동 탐색 및 조건
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue
            if dist[nx][ny] != 0:
                continue

            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

    return -1

"""
#DFS
import sys
sys.setrecursionlimit(10**6) #재귀 깊이 제한 늘림

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dist = [[float('inf')] * m for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x,y,d):
        if d >= dist[x][y]:
            return
        dist[x][y] = d

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 0:
                continue

            dfs(nx, ny, d + 1)
    dfs(0, 0, 1)

    result = dist[n-1][m-1]
    if result == float('inf'):
        return -1
    else:
        return result
"""

