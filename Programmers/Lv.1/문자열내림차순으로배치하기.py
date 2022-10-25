# https://school.programmers.co.kr/learn/courses/30/lessons/12917
# 코딩테스트연습 < 연습문제 < 문제.문자열 내림차순으로 배치하기



# 입력
'''
1. 문자열 s
- s는 영문 대소문자로만 구성
- 대문자는 소문자보다 작은 것으로 간주
'''



# 출력
'''
1. 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴
'''



# 코드
import sys

sys.stdin = open('input_text/문자열내림차순으로배치하기.txt')

def solution(s):
    return ''.join(sorted(s, reverse=True))


# 실행 결과: 성공