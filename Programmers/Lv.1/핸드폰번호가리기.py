# https://school.programmers.co.kr/learn/courses/30/lessons/12948
# 코딩테스트연습 < 연습문제 < 문제.핸드폰 번호 가리기



# 입력
'''
1. 전화번호가 문자열 phone_number
- 4 <= phone_number <= 20
'''



# 출력
'''
1. 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
'''


# 코드 
import sys

sys.stdin = open('input_text/핸드폰번호가리기.txt')

def solution(phone_number):
    return '*' * (len(phone_number) - 4) + phone_number[-4:]


# 실행 결과: 성공