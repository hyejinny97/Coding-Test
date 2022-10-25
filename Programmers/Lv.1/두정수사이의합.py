# https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 코딩테스트연습 < 연습문제 < 문제.두 정수 사이의 합



# 입력
'''
1. 두 정수 a, b
- -10,000,000 <= a, b <= 10,000,000
- a와 b의 대소관계는 정해져있지 않습니다.
'''



# 출력
'''
1. a와 b 사이에 속한 모든 정수의 합을 리턴
- a와 b가 같은 경우는 둘 중 아무 수나 리턴
'''



# 코드 1
import sys

sys.stdin = open('input_text/두정수사이의합.txt')

def solution(a, b):
    answer = 0
    for num in range(min(a, b), max(a, b) + 1):
        answer += num
    return answer


# 실행 결과: 성공




# 코드 2
# 참고(시그마): https://m.blog.naver.com/biomath2k/221847659166
import sys

sys.stdin = open('input_text/두정수사이의합.txt')

def solution(a, b):
    return (abs(a - b) + 1) * (a + b) // 2


# 실행 결과: 성공