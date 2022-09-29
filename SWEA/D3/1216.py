# 문제1216번.회문2
# 시간: 30초, 메모리: 256MB


# 입력
"""
<총 10개의 테스트 케이스 T>
1. 테스트 케이스 번호
2. 100x100 크기의 글자판
"""


# 출력
"""
1. #{테스트케이스} {가로, 세로를 모두 보아 가장 긴 회문의 길이}
- 가로 또는 세로로 이어진 회문의 개수만 세야함
- A또한 길이 1짜리 회문
"""


# 코드 1
import sys

sys.stdin = open("../input_text/1216.txt")

# 주어진 단어가 회문 구조인지 확인
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


# 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기
def find_palindrome(row):
    # 100글자부터 2글자까지 슬라이딩
    for length in range(100, 2 - 1, -1):
        # print(length)
        for c in range(0, (100 - length) + 1):
            # print(c, len(row[c : c + length]))
            if is_palindrome(row[c : c + length]):
                return length
    return 1


T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    max_palindrome = 1  # 가장 긴 회문의 길이

    # 100 x 100 크기의 글자판 입력받아 2차원 리스트로 구현
    matrix = [input() for _ in range(100)]

    # 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기
    for row in matrix:
        length = find_palindrome(row)
        max_palindrome = max(max_palindrome, length)

    # 글자판 행렬 뒤집기
    new_matrix = [[None] * 100 for _ in range(100)]
    for c in range(100):
        for r in range(100):
            new_matrix[c][r] = matrix[r][c]

    # 글자판의 열을 순회하면서 가장 긴 회문의 길이 찾기
    for row in new_matrix:
        length = find_palindrome(row)
        max_palindrome = max(max_palindrome, length)

    print(f"#{test_case} {max_palindrome}")


# 실행 결과: 성공(메모리:71,704 kb, 시간:2,570 ms)


# 코드 2 - 코드 1 리팩토링
import sys

sys.stdin = open("../input_text/1216.txt")

# 주어진 단어가 회문 구조인지 확인
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


# 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기
def find_palindrome(row, max_length):
    # 100글자부터 2글자까지 슬라이딩
    for length in range(100, max_length - 1, -1):
        # print(length)
        for c in range(0, (100 - length) + 1):
            # print(c, len(row[c : c + length]))
            if is_palindrome(row[c : c + length]):
                return length
    return 1


T = 10
for _ in range(1, T + 1):
    test_case = int(input())
    max_palindrome = 1  # 가장 긴 회문의 길이

    # 100 x 100 크기의 글자판 입력받아 2차원 리스트로 구현
    matrix = [input() for _ in range(100)]

    # 글자판의 행을 순회하면서 가장 긴 회문의 길이 찾기
    for row in matrix:
        length = find_palindrome(row, max_palindrome)
        max_palindrome = max(max_palindrome, length)

    # 글자판 행렬 뒤집기
    new_matrix = [[None] * 100 for _ in range(100)]
    for c in range(100):
        for r in range(100):
            new_matrix[c][r] = matrix[r][c]

    # 글자판의 열을 순회하면서 가장 긴 회문의 길이 찾기
    for row in new_matrix:
        length = find_palindrome(row, max_palindrome)
        max_palindrome = max(max_palindrome, length)

    print(f"#{test_case} {max_palindrome}")


# 실행 결과: 성공(메모리:71,968 kb, 시간:2,232 ms)
