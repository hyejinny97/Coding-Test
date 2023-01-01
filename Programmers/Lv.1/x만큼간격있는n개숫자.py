# https://school.programmers.co.kr/learn/courses/30/lessons/12954
# 코딩테스트연습 < 연습문제 < 문제.x만큼 간격이 있는 n개의 숫자



# 입력
'''
1. 정수 x, 자연수 n
- -10,000,000 <= x <= 10,000,000
- 0 < n <= 1,000
'''



# 출력
'''
1. x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴
'''



# 코드 1
import sys

sys.stdin = open('input_text/n개만큼간격있는n개숫자.txt')

def solution(x, n):
    last = -1 if x < 0 else 1
    return list(range(x, x * n + last, x))


# 실행 결과: 부분 성공(테스트 8번 런타임 에러)



# 코드 2
import sys

sys.stdin = open('input_text/n개만큼간격있는n개숫자.txt')

def solution(x, n):
    return [x * i for i in range(1, n + 1)]


# 실행 결과: 성공