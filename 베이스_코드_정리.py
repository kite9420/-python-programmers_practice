#2026/06/16 공부하며 모아둔 알고리즘 기본 골조들입니다.


#1. 다익스트라(heapa) : 한 점에서 모든 점까지의 최단 거리를 구하는 방법. 단, 비용이 있고 음수가 없을 때 사용.
#정점과 정점 사이의 연결과 비용을 담은 자료, 시작 정점, 모든 정점 개수를 입력으로 받음

from collections import defaultdict

def build_graph(edges: list[tuple[int]],n : int):
    graph = defaultdict(list) #존재하지 않는 키에 접근시 리스트 형태로 자동 생성
    for u,v,w in edges:
        graph[u].append((v,w))
        graph[v].append((u,w)) #양방향 간선
    return graph

import heapq
def dijkstra(graph, start, n):
    INF = float('inf')
    dist = [INF] * n
    dist[start] = 0
    heap = [(0,start)]  # 최단거리 순으로 정렬하기 위해 거리를 앞에 넣음
    while heap:
        d,u = heapq.heapop(heap)
        if d > dist[u] : #이미 더 짧은 경로가 존재하는 경우 스킵, visited와 같은 역활
            continue
        for v,w in graph[u]:
            nd = d + w
            if nd < dist[v]:   #무한 루프를 막아주는 부분. 새 조건이 기존 조건보다 짧을 때만 갱신
                dist[v] = nd
                heapq.heappush(heap,(nd,v))
    return dist


#2 플로이드- 워셜 : 모든 점에서 모든 점까지의 최단거리를 한번에 구하기. 삼중 반복문을 사용하므로 O(N^3)의 시간 복잡도를 가짐
# 결과표는 아래와 같은 2차원 배열로 출력됨

'''
        도착0  도착1  도착2  도착3
출발0 [   0    5     3     4  ]
출발1 [   5    0     ...  ...  ]
출발2 [   3    ...   0    ...  ]
출발3 [   4    ...   ...   0  ]
'''

def floyd_warshall(n, edges):
    INF = float('inf')
    dist = [[INF] * n  for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u,v,w, in edges:
        dist[u,v] = min(dist[u][v], w) #중복 간선이 있을 수 있으므로 min 사용
    for k in range(n): #k는 반드시 바깥 루프 -> k가 고정이 안되면 dist[k][k]값이 계산 안돼서 논리구조가 망가짐. 최단 경로는 같은 점을 두번 거치지 않으므로 k=0을 거친 후 k =1을 거친게 역으로 영향을 주지 않음
        for i in range(n):
            for j in range(n):
                if dist[i][k]+dist[k][j] < dist[i][j]:   #dist[i][j] -> i에서 j로 직접 가는 비용, k -> 경유지, k라는 경유지를 거치면 직접 가는것보다 짧은지 검사 (고정된 k에 대해 모든 i,j쌍을 검사)
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
        

#3 이분탐색 : 정확히 일치하는 값 찾기(일치 탐색, 인덱스 활용)
scores = [42, 55, 63, 71, 78, 85, 90, 97] # = arr, 오름차순 정렬 리스트.
def binary_search(arr: list[int], target: int):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return arr[mid]
        elif arr[mid] < target:
            lo = mid + 1
        else:
            lo = mid - 1
    return -1

#4 이분탐색 : Lower_bound #target의 값 이상/이하인 값이 나오는 인덱스 찾기
def lower_bound(arr: list[int], target : int):
    lo, hi = 0, len(arr)
    while lo < hi: #구간은 그때 그때 생각해서 설정 (~이상인 경우, ~보다 많은 경우 등)
        mid = (lo + hi) //2
        if arr[mid] < target:  #조건부
            lo = mid + 1
        else:
            hi = mid #mid 도 후보에 넣기 위해서
    return lo   #미묘하게 다르지만 기본 골조 lo, hi, mid 및 조건부 구조는 동일

#5 이분탐색 파라메트릭 서치(재귀사용 버전) : 답 자체를 이분. "최댓값의 최솟값", "최솟값의 최댓값", "조건을 만족하는 최대/최소 ___ 구하기". "x를 정하면 가능/불가능을 판정할 수 있고, 그 판정이 한쪽으로 단조"면 기계적으로 쓰기
# 재귀버전
#단, 판단 결과가 한 방향으로 바뀌는 단조식이여야 사용 가능하다. (어떤 x에 대해 x이상이면 가능, 이하이면 불가능으로 경계가 존재할 때. x^2 (-inf,inf) 같은 구간은 사용 불가
#판정함수 X
def check(x): #bool
    return x * x <= n
def parametric_search(lo, hi, check):
    # check(x): 조건 만족 시 True. True/False가 한쪽으로 단조여야 함.
    # "조건을 만족하는 최솟값 x"를 찾는 형태
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid                # mid 포함 후보
        else:
            lo = mid + 1
    return lo