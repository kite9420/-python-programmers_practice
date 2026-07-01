#2026/07/01
#소수 찾기
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42839
#문제 - 아직도 combiantion 같은 재귀문을 구현할 때 외부의 도움 및 문제 수정이 필요함. 통째로 외우거나, 다른 방법의 공부가 필요
#생각한 알고리즘 -> 소수 판정 / 재귀문을 통한 조합 찾기 / 조합이 소수이면 set에 추가 후 개수를 리턴 - 을 코드로 명확하게 구현하지 못함

def decimal(numbers):
    if numbers <= 1:
        return False
    root = int(numbers ** 0.5)
    for i in range(2, root +1):
        if numbers % i == 0:
            return False
    return True

def solution(numbers):
    leng= len(numbers)
    cand = []
    def combination(pick,remain):
        if pick:
            cand.append(pick)
        if not remain:
            cand.append(pick)
            return
        for i in range(len(remain)):
            combination(pick + [remain[i]] , remain[:i] + remain[i+1:])
    combination([],numbers)
    
    answer = set()
    for lst in cand:
        num = int("".join(lst))
        if decimal(num):
            answer.add(num)
    
    return len(answer)


'''
백트래킹? 을 이용한 더 효율적인 조합  코드
'매번 새 리스트를 만드는 대신, 하나의 리스트를 계속 재사용하면서 넣었다 뺐다(backtrack) 한다'
-> 리스트 슬라이싱이 없어져서 더 빨라짐
사용 여부를 외부의 TFF, TFT등의 bool 처리해서 상태를 관리함 -> 머리속 시뮬레이션이 따라가지를 못하는데?? 어떻게 구조를 짜야하는가
AI 추천 사고방식 -> 전체 시뮬레이션 대신 각각의 동작 패턴만 추적할 것, 트리구조 그려보기, append/pop이 스택처럼 쌓인다, 각각의 과정을 print로 확인하며 과정 고쳐나가기

패턴
들어갈 때: 상태에 뭔가 추가
재귀 호출
나올 때: 방금 추가한 거 제거


트리구조
[]
        /      |      \
      [1]     [2]     [3]
     /   \    /  \    /  \
  [1,2] [1,3] ...



def combination(pick, used):
    if pick:
        cand.append(pick[:])   # 저장할 때만 복사
    if len(pick) == leng:
        return
    for i in range(leng):
        if not used[i]:
            used[i] = True
            pick.append(numbers[i])
            combination(pick, used)
            pick.pop()
            used[i] = False

used = [False] * leng
combination([], used)

'''