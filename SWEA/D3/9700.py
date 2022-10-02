# 문제9700번.USB 꽂기의 미스터리
# 시간: 2초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 확률 p, q
- 0 <= p, q <= 1
"""


# 출력
"""
1. #{테스트케이스} {s1< s2 이면 “YES”를 아니면 “NO”를 출력}
- si: USB를 정확히 i번 뒤집었을 때 USB가 꽂힐 확률
- p: 가장 처음 USB를 쥘 때, 올바른 면으로 USB를 쥐고 있을 확률
- (1 - p): 가장 처음 USB를 쥘 때, 뒤집어서 USB를 쥐고 있을 확률
- q: 만약 올바른 면으로 USB를 쥐었을때, 정상적으로 USB가 꽂힐 확률
- (1 - q): 만약 올바른 면으로 USB를 쥐었을때, 정상적으로 USB가 꽂히지 않을 확률
(USB를 뒤집어져 쥐었다면 절대로 꽂히지 않음)
- USB를 꽂는 것을 실패하면 USB를 뒤집은 다음 다시 꽂는 것을 시
"""


# 접근방법
"""
1. s1 (USB를 정확히 1번 뒤집었을 때 USB가 꽂힐 확률)
- 가장 처음 뒤집어서 쥔 후, 1번 뒤집어서 정상적으로 USB를 꽂음
s1 = (1 - p) * q

2. s2 (USB를 정확히 2번 뒤집었을 때 USB가 꽂힐 확률)
- 가장 처음 올바른 면으로 쥔 후, 꽂히지 않아서 1번 뒤집고 또다시 1번 뒤집어서 정상적으로 USB를 꽂음
s2 = p * (1 - q) * q
"""


# 코드
import sys

sys.stdin = open("../input_text/9700.txt")

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(float, input().split())

    s1 = (1 - p) * q
    s2 = p * (1 - q) * q

    if s1 < s2:
        print(f"#{test_case} YES")
    else:
        print(f"#{test_case} NO")


# 실행 결과: 성공(메모리:56,792 kb, 시간:125 ms)
