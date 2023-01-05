# https://school.programmers.co.kr/learn/challenges?order=acceptance_desc&page=1&languages=python3&levels=2
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[1차] 캐시



# 입력
'''
1. 캐시 크기(cacheSize), 도시이름 배열(cities)
- 1 <= 캐시크기 <= 30
- 0 < 도시이름 배열 크기 <= 100,000
- 0 < 도시이름 크기 <= 20
- 도시이름: 공백, 숫자, 특수문자 등이 없는 영문자이고 대소문자 구분 x
'''



# 출력
'''
1. 입력된 도시이름 배열을 순서대로 처리할 때, "총 실행시간"을 출력
<조건>
- 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용
- cache hit일 경우, 실행시간은 1
- cache miss일 경우, 실행시간은 5
--------------------------------------------------------------
<LRU 알고리즘 (Least Recently Used Algorithm)>
- LRU 알고리즘 : 가장 오랫동안 참조되지 않은 페이지를 교체하는 기법
- LRU 참고: https://j2wooooo.tistory.com/121
'''



# 코드 1

# 접근방법
'''
deque 자료구조를 이용해 city를 push, pop
- deque 참고1: https://ooeunz.tistory.com/31
- deque 참고2: https://dongdongfather.tistory.com/72
'''

import sys
from collections import deque

sys.stdin = open('input_text/1차캐시.txt')

def solution(cacheSize, cities):
    runtime = 0
    q = deque([])
    for city in cities:
        city = city.lower()
        if city not in q:
            if q and len(q) == cacheSize:
                q.popleft()
            runtime += 5
        else:
            q.remove(city)
            runtime += 1
        q.append(city)
    return runtime


# 실행 결과: 성공



# 코드 2

# 접근방법
'''
deque 자료구조의 maxlen 속성 이용
- deque 참고: https://skeo131.tistory.com/76
'''

import sys
from collections import deque

sys.stdin = open('input_text/1차캐시.txt')

def solution(cacheSize, cities):
    runtime = 0
    q = deque([], maxlen=cacheSize)
    for city in cities:
        city = city.lower()
        if city not in q:
            runtime += 5
        else:
            q.remove(city)
            runtime += 1
        q.append(city)
    return runtime


# 실행 결과: 성공