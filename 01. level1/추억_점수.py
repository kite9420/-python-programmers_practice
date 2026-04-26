#2026/04/26
#추억 점수
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/176963
#컴프리헨션 버전

def solution(name,yearning, photo):
    scores = dict(zip(name,yearning))
    return[sum(scores.get(p,0) for p in persons) for persons in photo]

'''
def solution(name, yearning, photo):
    scores = {}
    result = []
    for i in range(len(name)):
        person = name[i]
        score = yearning[i]
        scores[person] = score

    for i in range(len(photo)):
        sums = 0
        for j in range(len(photo[i])):
            sums += scores.get(photo[i][j],0)
        result.append(sums)

    return result
'''