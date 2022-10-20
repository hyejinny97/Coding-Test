# https://school.programmers.co.kr/learn/courses/30/lessons/12919
# 코딩테스트연습 < 연습문제 < 문제.서울에서 김서방 찾기



# 입력
'''
1. String형 배열 seoul
- 1 <= 배열 길이 <= 1,000
- 1 <= 문자열 길이 <= 20
'''



# 출력
'''
1. String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환
'''



# 코드 
import sys

sys.stdin = open('input_text/서울에서김서방찾기.txt')

def solution(seoul):
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'


# 실행 결과: 성공