# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 코딩테스트연습 < 해시 < 문제.완주하지 못한 선수



# 입력
'''
1. 마라톤에 참여한 선수들의 이름이 담긴 배열 participant, 완주한 선수들의 이름이 담긴 배열 completion
- 1 <= 선수의 수 <= 100,000
- participant의 길이 = completion의 길이 - 1
- 1 <= 참가자의 이름 길이 <= 20
- 참가자 중에는 동명이인이 있을 수 있습니다.
'''



# 출력
'''
1. 완주하지 못한 선수의 이름을 return
'''



# 코드 1
import sys

sys.stdin = open('input_text/완주하지못한선수.txt')

def solution(participant, completion):
    check = dict()   # 키:사람, 값:인수
    
    # 참가자 체크
    for person in participant:
        if person not in check:
            check[person] = 1
        else:
            check[person] += 1
    
    # 완주자 체크
    for person in completion:
        check[person] -= 1
    
    # 완주하지 못한 사람
    for person in check:
        if check[person]:
            return person
        

# 실행 결과: 성공



# 참고(collections.Counter()): https://hongl.tistory.com/35
# 코드 2
import sys
from collections import Counter

sys.stdin = open('input_text/완주하지못한선수.txt')

def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    return list(answer.keys())[0]
    
# 실행 결과: 성공