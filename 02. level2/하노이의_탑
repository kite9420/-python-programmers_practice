
#2026/06/26
#하노이의 탑
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12946

#Hanoi(n)은 Hanoi(n-1)을 옮겨 가장 아래판을 빼내고 다시 Hanoi(n-1)을 그 위에 옮기는 방법임
#Hanoi(n) = 2 * Hanoi (n-1) + 1
#마찬가지로 순서는 이전 하노이쌍을 3번 기둥이 아닌 2번 기둥에 먼저 완성하고, 다시 옮기게 됨

def solution(n):
    def swap23(x): #경우지와 도착지를 바꾸는 함수
        if x == 2:
            return 3
        if x == 3:
            return 2
        return x
    def swap12(x):        
        if x == 1:
            return 2
        if x == 2:
            return 1
        return x
        
    def Hanoi(n) :
        if n == 2:
            return [ [1,2], [1,3], [2,3] ]
        temp = []
        for a,b in Hanoi(n-1): #123을 132 순서로
            temp.append([swap23(a),swap23(b)])
        temp.append([1,3])
        for a,b in Hanoi(n-1): #123을 213순서로
            temp.append([swap12(a),swap12(b)])
        return temp
    return Hanoi(n)

'''
다듬은 버전
def solution(n):
    def swap(x,a,b):
        if x == a:
            return b
        if x == b:
            return a
        return x
    def Hanoi(n) :
        if n == 1:
            return [[1,3]]
        prev = Hanoi(n-1)
        moves = []
        for a,b in prev:
            moves.append([swap(a,2,3),swap(b,2,3)])
        moves.append([1,3])
        for a,b in prev:
            moves.append([swap(a,1,2),swap(b,1,2)])
        return moves
    return Hanoi(n)
'''
#경유지 및 도착지를 사용한 버전
def solution(n):
    def hanoi(n,start,mid,end):
        if n == 0:
            return []
        return hanoi(n-1,start,end,mid) + [[start,end]] + hanoi(n-1,mid,start,end)
    return hanoi(n,1,2,3)