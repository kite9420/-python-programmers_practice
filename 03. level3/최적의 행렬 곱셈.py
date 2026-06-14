#2026/06/14
#최적의 행렬 곱셈
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12942

def solution(matrix_sizes):
    indexed = [matrix_sizes[0][0]] + [b for a,b in matrix_sizes]
    #indexed = [5, 3, 10, 6], n번째 행렬 = indexed[n-1] * indexed[n]
    #cost[i][j]는 두 행렬 사이의 최소비용, k는 순서를 바꾸는 위치(k = 1 이면 A/BC k = 2 이면 AB/C) = 1에서 쪼개면 (1,1) = A (2,3) = BC
    #최소 비용 = cost[i][k] + cost[k+1][j] + indexed[i-1]*indexed[k]*indexed[j]
    
    dict_c = {}
    def cost(i,j):
        if (i,j) in dict_c:
            return dict_c[i,j]
        if i == j:
            return 0
        
        total_cost = float("inf")
        for k in range(i,j):
            cur = cost(i, k) + cost(k+1, j) + indexed[i-1]*indexed[k]*indexed[j]
            if cur < total_cost:
                total_cost = cur
        dict_c[(i,j)] = total_cost
        return total_cost
    return cost(1,len(matrix_sizes))
    
''' 반복문 형태
def solution(matrix_sizes):
    indexed = [matrix_sizes[0][0]] + [b for a,b in matrix_sizes]
    n = len(matrix_sizes)
    
    cost = [[0]*(n+1) for _ in range(n+1)]

    for length in range(2, n+1):
        for i in range(1, n- length +2):
            j = i + length-1
            cost[i][j] = float("inf")
            for k in range(i,j):
                cur = cost(i, k) + cost(k+1, j) + indexed[i-1]*indexed[k]*indexed[j]
                if cur < cost[i][j]:
                    cost[i][j] = cur
    return cost[1][n]
'''