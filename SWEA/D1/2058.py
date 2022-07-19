# 문제2058.자릿수 더하기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 자연수 N
- 1 <= N <= 9999
'''

# 출력
'''
각 자릿수의 합을 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2058.txt', 'r')

N = int(input())
rst = 0
while N:
    rst += N % 10
    N //= 10
print(rst)

# 실행 결과: 성공(메모리:56,672 kb, 시간:136 ms)