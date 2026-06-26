#2026/06/26
#2019_카카오_튜플
#문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    s = s[2:-2].split('},{')
    listed = [[int(x) for x in i.split(',')] for i in s]
    listed.sort(key=len)
    answer = []
    seen = set()
    for i in listed:
        for j in i:
            if j not in seen:
                seen.add(j)
                answer.append(j)
                break
    return answer

#아래는 Counter를 사용한 코드 - 빈도수 이용
from collections import Counter
def solution(s):
    nums = s[2:-2].replace('},{',',').split(',')
    count = Counter(map(int,nums))
    answer = []
    for n, _ in count.most_common():  # most_common() --> Counter를 (원소, 출현횟수) 튜플 리스트로, 출현 횟수 내림차순 정렬해서 반환
        answer.append(n)
    return answer
#컴프리헨션으로 return [n for n, _ in count.most_common()]


'''
c = Counter(['a', 'b', 'b', 'c', 'a', 'b'])
# Counter({'a': 2, 'b': 3, 'c': 1})

c.most_common()
# [('b', 3), ('a', 2), ('c', 1)]    전체, 횟수 내림차순

'''