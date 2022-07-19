# 문제1938.아주 간단한 계산기
# 시간: 4초, 메모리: 256MB

# 입력
'''
1. 자연수 2개 a, b
- 1 <= a, b <= 9
'''

# 출력
'''
1. 각 줄에 두 자연수 a, b를 차례대로 +, -, *, /한 결과를 출력
- 나누기 연산의 결과에서 소수점 이하의 숫자는 버림
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1938.txt', 'r')

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)

# 실행 결과: 성공(메모리:56,692 kb, 시간:126 ms)