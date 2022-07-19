# 문제2025.N줄 덧셈
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 정수 1개
- 정수 <= 10000
'''

# 출력
'''
1. 1부터 주어진 숫자만큼 모두 더한 값을 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2025.txt', 'r')

n = int(input())
print(sum(range(1, n + 1)))

# 실행 결과: 성공(메모리:56,940 kb, 시간:129 ms)