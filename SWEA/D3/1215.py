# 문제1215번.회문1
# 시간: 30초, 메모리: 256MB


# 입력
"""
<총 10개의 테스트 케이스 T>
1. 찾아야 하는 회문의 길이
2. 8x8 크기의 글자판
"""


# 출력
"""
1. #{테스트케이스} {찾은 회문의 개수}
- 가로 또는 세로로 이어진 회문의 개수만 세야함
"""


# 코드
import sys

sys.stdin = open("../input_text/1215.txt")

# 해당 글자가 회문구조면 True 반환
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False


# 글자판을 행 순회하면서 가로 방향의 회문 찾기
def find_palindrome(array):
    global length
    cnt = 0
    for r in range(0, 7 + 1):
        for c in range(0, (8 - length) + 1):
            if is_palindrome(array[r][c : c + length]):
                cnt += 1
                # print((r, c), array[r][c : c + 4])
    return cnt


T = 10
for test_case in range(1, T + 1):
    length = int(input())  # 찾아야하는 회문의 길이
    tot_cnt = 0  # 찾은 회문의 개수

    # 8 x 8 크기의 글자판을 2차원리스트로 생성
    matrix = [input() for _ in range(8)]

    # 가로 방향의 회문찾기
    tot_cnt += find_palindrome(matrix)

    # 글자판 행렬 바꾸기
    new_matrix = [[None] * 8 for _ in range(8)]
    for c in range(8):
        for r in range(8):
            new_matrix[c][r] = matrix[r][c]

    # 세로 방향의 회문찾기
    tot_cnt += find_palindrome(new_matrix)

    print(f"#{test_case} {tot_cnt}")


# 실행 결과: 성공(메모리:56,984 kb, 시간:114 ms)
