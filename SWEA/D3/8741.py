# 문제8741번.두 문자어
# 시간: 30초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 T
2. 영어 소문자로 이루어진 세 문자열
- 1 <= 문자열 길이 <= 20
"""


# 출력
"""
1. #{테스트케이스} {문자열의 앞글자를 대문자로 바꿔 순서대로 출력}
"""


# 코드
import sys

sys.stdin = open("../input_text/8741.txt")

T = int(input())
for test_case in range(1, T + 1):
    words = input().split()

    uppercase = ""
    for word in words:
        uppercase += word[0].upper()

    print(f"#{test_case} {uppercase}")


# 실행 결과: 성공()
