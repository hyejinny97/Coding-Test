# 문제8658번.Summation
# 시간: 초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. 자연수 10개
- 1 <= 자연수 <= 1,000,000
"""


# 출력
"""
1. #{테스트케이스} {10개의 자연수의 각 자리 수를 모두 더했을때 구해지는 최대값과 최소값}
"""


# 코드
import sys

sys.stdin = open("../input_text/8658.txt")


T = int(input())
for test_case in range(1, T + 1):
    nums = input().split()

    max_sum = 0
    min_sum = 9 * (10**6)
    for num in nums:
        # num의 각 자리수 더하기
        num_sum = 0
        for n in num:
            num_sum += int(n)

        # 최댓값 갱신
        max_sum = max(max_sum, num_sum)

        # 최솟값 갱신
        min_sum = min(min_sum, num_sum)

    print(f"#{test_case} {max_sum} {min_sum}")
