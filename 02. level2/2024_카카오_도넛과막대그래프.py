#2026/06/27
#2024_카카오_도넛과막대그래프
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/258711


#그냥 그래프 간선 특징을 쓰면 더 쉽지만 수학적인 방법이고 프로그래밍과는 먼 것 같기에 연습용으로 부적잘
from collections import defaultdict,deque
def solution(edges):
    dict_in = defaultdict(int)
    dict_out = defaultdict(int)
    root = 0
    for a,b in edges:
        dict_out[a] += 1
        dict_in[b] +=1
    for can in dict_out:
        if dict_out[can] >= 2 and can not in dict_in:
            root = can
            break
    
    graph = defaultdict(list)
    for a,b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    def count(start):
        q = deque([start])
        visited = {start}
        edge_count = 0
        while q:
            cur = q.popleft()
            for i in graph[cur]:
                if i == root:
                    continue
                edge_count += 1
                if i not in visited:
                    visited.add(i)
                    q.append(i)
        V = len(visited)
        E = 0
        for v in visited:
            E += dict_out[v]
        return V,E
    
    result = [root,0,0,0] #정점, 도넛, 막대, 8자
    for start in graph[root]:
        V, E = count(start)
        if V == E:
            result[1] += 1
        elif V == E + 1:
            result[2] += 1
        elif V == E - 1:
            result[3] += 1
        
    return result

#더 나은 코드
def solution(edges):
    #머리 찾기
    dict_in = defaultdict(int)
    dict_out = defaultdict(int)
    root = 0
    for a,b in edges:
        dict_out[a] += 1
        dict_in[b] +=1
    for can in dict_out:
        if dict_out[can] >= 2 and can not in dict_in:
            root = can
            break
    donut = bar = eight = 0
    for v in dict_out:
        if v == root:
            continue
        if dict_out[v] >= 2:
            eight += 1 #8자의 중앙점만이 나가는 간선이 2개이므로
    for v in dict_in:
        if v not in dict_out:
            bar += 1 #막대 그래프는 들어오는 간선으로는 나가지 않으므로
    donut = dict_out[root] - bar -eight #root에서 나가는 간선의 수는 총 그래프의 수
    return [root,donut,bar,eight]