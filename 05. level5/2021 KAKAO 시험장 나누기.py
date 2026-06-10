#2026/06/10
#시험장 나누기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/81305

'''접근 전략 : 
1.파라메트릭서치(이분탐색)
가장 큰 그룹의 인원(X)을 최소화" → "X 이하로 나눌 수 있는가?"라는 판정으로 변환
True or False의 판정을 만든 후 이분탐색(lo,hi 값을 좁혀나가며)으로 X를 찾음

2.DP(동적 계획법)
부모 계산을 작은 자식 계산들의 여러 결과로 쪼갤 수 있을 때 사용
bottom-up으로 자식 노드부터 계산하며 올라가며, 인원이 mid를 넘으면 무거운 자식 간선부터 끊어 mid 이하로 맞추는 방향으로 접근

공부 메모 
최댓값 최소화 혹은 최솟값 최대화 -> 파라메트릭 서치 (lo, hi 이용한 이분탐색)
부모가 자식 값에 의존 -> DP (동적 계획법 / 탑다운, 바텀엄 / 자식 혹은 부모의 값을 테이블 혹은 리스트에 기록)
트리인데 루트 안줌 -> 자식으로 안나온 루트 찾기
트리 순회는 기본 DFS(재귀/스택)
스택 - LIFO(후입선출 / pop)
큐  - FIFO(선입선출 /popleft)
재귀 -> 순서를 직접 지정할 필요가 없어 코드가 간단 / 단 깊이가 깊어지면 잘 터짐 / 백트래킹(막히면 다른 방향 시도시) 필요시 재귀 호출에서 관리할 수 있음
스택 -> 따로 메모할 곳을 만들어 하위 값들을 저장 / 단, 코드가 복잡해지고 순서를 사용자가 설정해야함
'''

def solution(k, num, links):
    n = len(num)
    # 1) 루트(머리 찾기)
    child = set()
    for a, b in links:
        child.add(a)
        child.add(b)
    root = (set(range(n)) - child).pop()
    
    # 2) 아래부터 올라가기 위해 순서 만들기 (재귀 터지는걸 막기 위해 스택 사용) 
    order = []
    stack = [root]
    while stack:
        i = stack.pop()
        order.append(i)
        for j in links[i]:
            if j != -1:
                stack.append(j)
    # order는 부모순으로 정렬됨
    
    # 3) 이분 탐색을 실행하기 전 X값이 조건을 충족하는지 판정하는 함수 만들기(스택)
    def check(mid):
        up = [0] * n     # 자식이 부모에게 올려다주는 그룹 인원의 수 (인덱스 = 시험장 번호)
        cut = [0] * n    # 자식 노드에서 자른 간선 수
        
        for i in reversed(order):  #i는 시험장 번호
            ups = [] #자식에서 올려준 값
            total_cut = 0
            cur = num[i] #자기 자신의 시험장 인원 수
            
            for c in links[i]: #루프를 통해서 ups에 자식 노드의 컷과 그룹 인원을 추가
                if c != -1:
                    ups.append(up[c])
                    cur += up[c]
                    total_cut += cut[c]
            ups.sort(reverse = True) #큰 자식부터 빼기 위해 재정렬
            idx = 0 #큰 순으로 정렬하였으므로 자식 노드의 시험장 번호 대신 인덱스를 사용하였음
            
            while cur > mid and idx <len(ups):  #자식 노드를 큰순부터 잘라내는 부분
                cur -= ups[idx]
                idx += 1
                total_cut += 1
            
            up[i] = cur
            cut[i] = total_cut
        
        return up[root] <= mid and cut[root] <= k-1
    

    ''' 재귀(DFS) 버전 판정함수 -> #2의 과정이 빠짐
    def check(mid):
        def dfs(i):
            cur = num(i)
            total_cut = 0
            ups = []

            for c in links[i]:
                if c != -1:
                    up_c, cut_c = dfs(c)
                    cur += up_c
                    total_cut += cut_c
                    ups.append(up_c)
                
            ups.sort(reverse = True)
            idx = 0

            while cur > mid and idx <len(ups):  #자식 노드를 큰순부터 잘라내는 부분
                cur -= ups[idx]
                idx += 1
                total_cut += 1

            return cur, total_cut

        up_root, cut_root = dfs(root)
        return up_root <= mid and cut_root <= k-1           
    '''
    
    # 4) 이분 탐색을 이용해서 answer 찾기
    lo, hi = max(num), sum(num)  #가장 큰 그룹은 가장 인원이 많은 시험장 인원을 넘을 수 없고, 가장 큰 그룹이라도 전체 인원수를 넘을 수 없음
    answer = hi
    while lo <= hi:
        mid = (lo + hi) //2
        if check(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    return answer