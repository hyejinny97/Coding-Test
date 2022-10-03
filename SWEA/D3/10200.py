# 문제10200번.구독자 전쟁
# 시간: 2초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 사람의 수 N, P 채널 구독자 수 A, T 채널 구독자 수 B
- 1 <= N <= 100
- 0 <= A, B <= N 
"""


# 출력
"""
1. #{테스트케이스} {P채널과 T채널 모두 구독하고 있는 사람의 수의 최댓값과 최솟값}
"""


# 코드
import sys

sys.stdin = open("../input_text/10200.txt", "rt", encoding="UTF8")

T = int(input())
for test_case in range(1, T + 1):
    N, A, B = map(int, input().split())

    max_val = min(A, B)
    min_val = 0 if A + B <= N else A + B - N

    print(f"#{test_case} {max_val} {min_val}")


# 실행 결과: 성공(메모리:61,684 kb, 시간:301 ms)
