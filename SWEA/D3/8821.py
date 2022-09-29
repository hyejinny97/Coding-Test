# 문제8821번.적고 지우기
# 시간: 30초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. ‘0’에서 ‘9’사이의 숫자로 이루어진 문자열 
- 1 <= 문자열 길이 <= 10,000
"""


# 출력
"""
1. #{테스트케이스} {마지막에 공책에 적힌 숫자의 개수}
- 공책에 숫자가 적혀있으면 지우고, 적혀있지 않으면 적음
"""


# 코드
import sys

sys.stdin = open("../input_text/8821.txt")

T = int(input())
for test_case in range(1, T + 1):
    nums = input()

    note = set()
    for n in nums:
        if n in note:
            note.remove(n)
        else:
            note.add(n)

    print(f"#{test_case} {len(note)}")


# 실행 결과: 성공(메모리:56,984 kb, 시간:114 ms)
