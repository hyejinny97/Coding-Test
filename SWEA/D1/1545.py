# 문제1545.거꾸로 출력해 보아요
# 시간: 4초, 메모리: 256MB

# 입력
'''
정수 1개
'''

# 출력
'''
입력된 정수부터 0까지 순서대로 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1545.txt', 'r')

N = int(input())
for i in range(N, 0 - 1, -1):
    print(i, end=' ')

# 실행 결과: 성공(메모리:56,676 kb, 시간:135 ms)