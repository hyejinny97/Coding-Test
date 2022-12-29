# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 코딩테스트연습 < 연습문제 < 문제.약수의 합



# 입력
'''
1. 정수 n
- 0 <= N <= 3,000
'''



# 출력
'''
1. n의 약수를 모두 더한 값을 리턴
'''



# 코드
import sys

sys.stdin = open('input_text/약수의합.txt')

def solution(N):
    answer = 0
    for n in range(1, int(N ** 0.5) + 1):
        if N % n == 0:
            answer += n
            if N // n != n:
                answer += N // n

    return answer


# 실행 결과: 성공