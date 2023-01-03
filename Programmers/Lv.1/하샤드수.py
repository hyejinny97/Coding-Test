# https://school.programmers.co.kr/learn/courses/30/lessons/12947
# 코딩테스트연습 < 연습문제 < 문제.하샤드 수



# 입력
'''
1. 양의 정수 x
- 1 <= x <= 10,000 
'''



# 출력
'''
1. 하샤드 수이면 true 반환, 아니면 false 반환 
- 하샤드 수: x의 자릿수의 합으로 x가 나눠지는 수
'''



# 코드 
import sys

sys.stdin = open('input_text/하샤드수.txt')

def solution(x):
    sum_digit = 0
    for num in str(x):
        sum_digit += int(num)
    return not x % sum_digit
        

# 실행 결과: 성공