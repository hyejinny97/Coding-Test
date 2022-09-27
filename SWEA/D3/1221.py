# 문제1221번.GNS
# 시간: 30초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. # + 테스트케이스 번호, 테스트케이스의 길이 N
3. N개의 단어
- 100 ≤  문자열의 길이 ≤ 10,000
- 단어: "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
- 위 단어는 각각 0~9의 값을 나타낸 것 
"""


# 출력
"""
1. #{테스트케이스} {정렬된 문자열}
"""


# 코드
import sys

sys.stdin = open("../input_text/1221.txt")

nums = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

T = int(input())
for _ in range(1, T + 1):
    test_case, N = input().split()
    words = input().split()

    # N개의 단어 정렬
    words.sort(key=lambda x: nums[x])

    print(test_case)
    print(*words)


# 실행 결과: 성공(메모리:64,312 kb, 시간:212 ms)
