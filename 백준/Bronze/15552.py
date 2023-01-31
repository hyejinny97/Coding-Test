# https://www.acmicpc.net/problem/15552
# 문제15552번.빠른 A+B
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 테스트케이스의 개수 T
- 0 < T <= 1,000,000
2. T개 줄에 A, B
- 1 <= A, B <= 1,000
'''



# 출력
'''
1. A+B를 한 줄에 하나씩 순서대로 출력
'''



# 코드
import sys

sys.stdin = open('input_text/15552.txt')

T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)


# 실행 결과: 성공(메모리:31256kb, 시간:1296ms)