# 문제9317번.석찬이의 받아쓰기
# 시간: 초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 문자열 길이 N
- 1 <= N <= 100,000
3. 석찬이가 따라서 적어야 하는 문자열
4. 석찬이가 받아 적은 문자열
"""


# 출력
"""
1. #{테스트케이스} {석찬이가 맞게 받아 적은 문자의 개수}
"""


# 코드
import sys

sys.stdin = open("../input_text/9317.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    expect = input()
    actual = input()

    cnt = 0
    for i in range(N):
        if expect[i] == actual[i]:
            cnt += 1

    print(f"#{test_case} {cnt}")
