#2026/06/06
#2025 프로그래머스 코드챌린지 2차 예선 완전범죄(DP)
#DP : Dynamic Programming, 동적 계획법. 문제를 작은 문제로 나누어 푸는 방법. 작은 문제의 답을 저장하여 큰 문제의 답을 구하는 방식
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/389480
# dp 문제. 각각의 아이템 선택에 대해 최종 선택지들을 계산하고 그중 조건에 맞는 값을 출력

def solution(info, n, m):
    current_set = {(0,0)}
    for i in range(len(info)):
        next_set = set()
        for (a,b) in current_set:
            new_a = a + info[i][0]
            if new_a < n:
                next_set.add((new_a,b))
            new_b = b + info[i][1]
            if new_b < m:
                next_set.add((a,new_b))
        current_set = next_set
    if len(current_set) == 0:
            return -1
    return min(a for a,b in current_set)

#용어 정리
#Memoization : 메모이제이션, 이미 계산한 결과를 저장하여 다시 계산하지 않도록 하는 방법. top-down 방식으로 문제를 해결할 때 사용
#Tabulation : 테이블레이션, 문제를 작은 문제로 나누어 테이블에 저장하여 해결하는 방법. bottom-up 방식으로 문제를 해결할 때 사용
#Top-down : 문제를 큰 문제에서 작은 문제로 나누어 해결하는 방식. 재귀적으로 문제를 해결, 메모이제이션을 사용하여 중복 계산을 방지
#Bottom-up : 문제를 작은 문제에서 큰 문제로 나누어 해결하는 방식. 반복문을 사용하여 문제를 해결, 테이블레이션을 사용하여 중복 계산을 방지

'''
피보나치 재귀/ Top-down 방식 / Bottom-up 방식 비교

1) 재귀 방식
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

2) Top-down 방식 (메모이제이션)
def fib(n, memo = {}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

3) Bottom_up 방식 (테이블레이션)
def fib(n):
    if n <= 1:
        return n
    dp = {} #이 문제에서는 리스트가 더 빠르지만 상태가 튜플이거나, 인덱스가 듬성듬성하게 찰 때에는 딕셔너리가 더 나음)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

'''
