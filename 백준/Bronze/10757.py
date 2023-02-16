# https://www.acmicpc.net/problem/10757
# 문제10757번.큰 수 A+B
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 두 정수 A, B
- 0 < A,B < 10^10000
'''



# 출력
'''
1. A+B를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10757.txt')

A, B = map(int, input().split())

print(A + B)


# 실행 결과: 성공(메모리:31256kb, 시간:44ms)