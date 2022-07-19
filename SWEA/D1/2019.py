# 문제2019.더블더블
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 숫자 1개
- 숫자 <= 30
'''

# 출력
'''
1. 1부터 주어진 횟수까지 2를 곱한 값들을 출력
'''

# 코드 
import sys

sys.stdin = open('SWEA/input_text/2019.txt', 'r')

n = int(input())
for i in range(n+1):
    print(2**i, end=' ')

# 실행 결과: 성공(메모리:56,672 kb, 시간:142 ms)