# https://www.acmicpc.net/problem/10869
# 문제10869번.사칙연산
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 정수 A, B
- 1 <= A,B <= 10,000
'''



# 출력
'''
1. A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10869.txt')

A, B = list(map(int, input().split()))
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)


# 실행 결과: 성공(메모리:30864kb, 시간:68ms)