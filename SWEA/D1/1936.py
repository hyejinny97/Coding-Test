# 문제1936.1대1 가위바위보
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. A와 B 두 명이 각자 가위바위보 중 무엇을 냈는지
- 가위=1, 바위=2, 보=3
'''

# 출력
'''
1. A와 B 중 이긴 사람을 출력
- 비기는 경우는 없음
'''

# 코드 
import sys

sys.stdin = open('SWEA/input_text/1936.txt', 'r')

a, b = map(int, input().split())
print('B' if b == (a + 1) % 3 else 'A')

# 실행 결과: 성공(메모리:56,672 kb, 시간:128 ms)