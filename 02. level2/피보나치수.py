#2026/07/04
#피보나치수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12945
#단순 피보나치가 아닌 모듈러 연산을 통한 효율화가 중요 -> 효율성 통과를 위해
#모듈러 연산의 수학적 증명:
"""
정의: x mod m = r  ⟺  x = qm + r,  0 ≤ r < m

주어진 것:
  a = q1*m + r1,  0 ≤ r1 < m
  b = q2*m + r2,  0 ≤ r2 < m
  ⇒ a+b = (q1+q2)*m + (r1+r2),  0 ≤ r1+r2 < 2m

경우 1: 0 ≤ r1+r2 < m

  a+b = (q1+q2)*m + (r1+r2)        [몫 = q1+q2, 나머지 = r1+r2 (0 ≤ r1+r2 < m)]
  ⇒ (a+b) mod m = r1+r2

  r1+r2 = 0*m + (r1+r2)
  ⇒ (r1+r2) mod m = r1+r2

  ∴ (a+b) mod m = (r1+r2) mod m

경우 2: m ≤ r1+r2 < 2m

  s := r1+r2 - m  ⇒  0 ≤ s < m

  a+b = (q1+q2)*m + (m+s) = (q1+q2+1)*m + s    [몫 = q1+q2+1, 나머지 = s]
  ⇒ (a+b) mod m = s

  r1+r2 = 1*m + s
  ⇒ (r1+r2) mod m = s

  ∴ (a+b) mod m = (r1+r2) mod m    ∎
"""
#-> 따라서 아래 함수에서 각 단계마다 1234567을 나누어도 문제가 되지 않으며, 첫 a,b는 1234567보다 작은 값이므로 문제가 되지 않음
#-> 또한 n >= 4인 경우부터는 a = 이전 단계에서 (a+b) % 1234567이 된 값이므로 모듈러 연산의 범위를 벗아나지 않음

'''
초기:      a=1,     b=1          (둘 다 초기값)
반복 1:    a=1,     b=(1+1)%m    (a는 아직 초기값)
반복 2:    a=(1+1)%m, b=(1+2)%m  (a가 처음으로 모듈러 결과가 됨)
반복 3:    a=이전 b,  b=(a+b)%m   (이후 계속)
'''

def solution(n):
    a, b  = 1, 1
    for _ in range(n-2):
        a, b = b, (a+b) % 1234567
    return b

'''기존 코드
def solution(n):
    memo = {1:1, 2,1}
    def fib(n):
        if n in memo:
            return memo[n]
        memo[n] = fib(n-1) + fib(n-2)
        reuturn momo[n]
    retrun fib(n) %1234567
'''