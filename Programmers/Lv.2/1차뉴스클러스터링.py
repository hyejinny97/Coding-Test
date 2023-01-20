# https://school.programmers.co.kr/learn/courses/30/lessons/17677
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[1차] 뉴스 클러스터링



# 입력
'''
1. 두 문자열 str1, str2
- 2 <= 문자열 길이 <= 1,000
- 문자열을 각각 두 글자씩 끊어서 다중집합의 원소로 만듦
- 영문자로 된 글자 쌍만 유효
- 타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버림
- 대문자와 소문자의 차이는 무시
'''



# 출력
'''
1. 두 문자열의 자카드 유사도를 출력
- 0 <= 유사도 <= 1
- 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력

<자카드 유사도>
- 집합 간의 유사도를 검사하는 여러 방법 중의 하나
- 두 집합 A, B 사이의 자카드 유사도 J(A, B) = 두 집합의 교집합 크기를 두 집합의 합집합 크기로 나눈 값
- 집합 A와 집합 B가 모두 공집합일 경우, J(A, B) = 1
- 자카드 유사도는 원소의 중복을 허용하는 다중집합에 대해서 확장 가능
'''



# 코드 
import sys
from collections import Counter
import re

sys.stdin = open('input_text/1차뉴스클러스터링.txt')

def solution(str1, str2):
    # 문자열을 두 글자씩 끊어서 다중집합 만들기
    set1, set2 = [], []
    p = re.compile('[a-z]{2}')
    for i in range(0, len(str1)):
        two_chars = str1[i:i+2].lower()
        if p.match(two_chars):
            set1.append(two_chars)
    for i in range(0, len(str2)):
        two_chars = str2[i:i+2].lower()
        if p.match(two_chars):
            set2.append(two_chars)

    # 다중집합 내 원소 개수 세기
    set1 = Counter(set1)
    set2 = Counter(set2)

    # 교집합, 합집합 원소 개수 구하기
    intersection = 0
    for two_chars in set1:
        intersection += min(set1.get(two_chars), set2.get(two_chars, 0))
    union = sum(set1.values()) + sum(set2.values()) - intersection

    # 자카드 유사도 구하기
    if union:
        jaccard_similarity = intersection / union
    else: 
        jaccard_similarity = 1

    return int(jaccard_similarity * 65536)


# 실행 결과: 성공