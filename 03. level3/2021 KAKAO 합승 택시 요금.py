#2026/06/14
#2021 KAKAO 합승 택시 요금
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72413


from collections import defaultdict
import heapq

'''
간선 문제 + 특정 지점에서 두 간선으로 분리
아이디어 -> 모든 노드 간의 최단 거리를 미리 구해놓기
or  출발지에서 모든 지점까지의 최단거리 구하기 + 두 사람의 목적지에서 최단거리 구하기
기계적 풀이법 -> 한 정점에서 다른 모든점 : 디익스트라 / 모든 정점에서 다른 모든 정점 : 플로이드 워셜
디익스트라를 이용해 각 지점 (출발지,a,b) 에서 각 노드까지의 최단거리를 구한 뒤 세 합의 최솟값을 구하는 방식으로 결정
'''

def solution(n, s, a, b, fares):
    def build_graph(fares, n):
        graph = defaultdict(list)
        for a,b,d in fares:
                graph[a].append((b,d))
                graph[b].append((a,d))
        return graph
            
    def dijkstra(graph,start,n):
        INF = float('inf')
        dist = [INF] * (n+1)
        dist[start] = 0
        heap = [(0,start)]
        
        while heap:
            dis, cur = heapq.heappop(heap)
            if dis > dist[cur]:
                continue
            for v, w in graph[cur]:
                nd = dis + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap,(nd,v))
        return dist
    
    graph = build_graph(fares,n)
    
    dist_s = dijkstra(graph,s,n)
    dist_a = dijkstra(graph,a,n)
    dist_b = dijkstra(graph,b,n)
    
    result = float('inf')
    for i in range(n+1):
        if dist_s[i] + dist_a[i] + dist_b[i] < result:
            result = dist_s[i] + dist_a[i] + dist_b[i]
    return result
                