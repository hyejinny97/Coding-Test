# https://school.programmers.co.kr/learn/courses/30/lessons/12901
# 코딩테스트연습 < 연습문제 < 문제.2016년



# 입력
'''
1. 두 수 a ,b
'''



# 출력
'''
1. 2016년 a월 b일이 무슨 요일인지 리턴
- 2016년 1월 1일은 금요일
- 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT
- 2016년은 윤년
'''



# 코드 
import sys

sys.stdin = open('input_text/2016년.txt')

def solution(a, b):
    # months => 인덱스:월, 값:해당 월이 며칠인지
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   
    # 2016년 1월 1일은 금요일이므로 인덱스 1번째는 금요일
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', ]
    
    # 2016년 a월 b일이 무슨 요일인지 리턴
    tot = sum(months[:a]) + b   # 1월1일로부터 총 며칠이 지났는지

    return days[tot % 7]


# 실행 결과: 성공