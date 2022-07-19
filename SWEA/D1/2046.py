# 문제2046.스탬프 찍기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 숫자
- 숫자 <= 100,000
'''

# 출력
'''
1. 주어진 숫자만큼 #을 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2046.txt', 'r')

n = int(input())
print('#' * n)

# 실행 결과: 성공(메모리:56,708 kb, 시간:134 ms)
