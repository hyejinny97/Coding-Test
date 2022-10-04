# 문제4613번.러시아 국기 같은 깃발
# 시간: 4초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. N행 M열
- 3 <= N, M <= 50
3. N개의 줄에 M개의 문자열
- ‘W’는 흰색, ‘B’는 파란색, ‘R’은 빨간색
"""


# 출력
"""
1. #{테스트케이스} {러시아 국기 같은 깃발을 만들기 위해서 새로 칠해야 하는 칸의 개수의 최솟값}
<조건>
- 위에서 몇 줄(한 줄 이상)은 모두 흰색으로 칠해져 있어야 한다.
- 다음 몇 줄(한 줄 이상)은 모두 파란색으로 칠해져 있어야 한다.
- 나머지 줄(한 줄 이상)은 모두 빨간색으로 칠해져 있어야 한다.
"""


# 코드 1
import sys

sys.stdin = open("../input_text/4613.txt")


def coloring(white, blue, red):
    row, col = len(matrix), len(matrix[0])
    cnt = 0
    for r in range(row):
        for c in range(col):
            # 현재 행에 칠해야 하는 색깔 구하기
            if r < white:
                color = "W"
            elif r < (white + blue):
                color = "B"
            elif r < (white + blue + red):
                color = "R"

            # 행 색깔에 맞춰 새로 칠하기
            if matrix[r][c] != color:
                cnt += 1

    return cnt


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N행 M열 깃발
    matrix = [input() for _ in range(N)]

    # 줄마다 색칠
    min_cnt = N * M  # 색칠 수 최솟값
    for w in range(1, N - 1):  # 흰색 줄 개수
        for b in range(1, N - w):  # 파란색 줄 개수
            r = N - w - b  # 빨간색 줄 개수
            cnt = coloring(w, b, r)  # 색칠 수
            min_cnt = min(min_cnt, cnt)

    print(f"#{test_case} {min_cnt}")


# 실행 결과: 성공(메모리:62,228 kb, 시간:316 ms)


# 코드 2
import sys

sys.stdin = open("../input_text/4613.txt")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # N행 M열 깃발
    matrix = [input() for _ in range(N)]

    # 깃발의 각 행의 w, b, r 갯수를 세서 누적
    new_matrix = []
    for row in matrix:
        w = row.count("W")
        b = row.count("B")
        r = M - w - b
        new_matrix.append([w, b, r])
    for i in range(1, N):
        new_matrix[i][0] += new_matrix[i - 1][0]
        new_matrix[i][1] += new_matrix[i - 1][1]
        new_matrix[i][2] += new_matrix[i - 1][2]

    # 줄을 계속 다르게 설정하면서 각 줄의 존재해야하는 색과 동일한 색인 경우 카운트 -> w, b, r 모두 합친 최댓값 구하기
    max_color = 0
    for i in range(N - 2):  # i: 흰색 줄 개수
        for j in range(i + 1, N - 1):  # j - i: 파란색 줄 개수
            white = new_matrix[i][0]
            blue = new_matrix[j][1] - new_matrix[i][1]
            red = new_matrix[N - 1][2] - new_matrix[j][2]
            max_color = max(max_color, white + blue + red)

    # 새로 칠해야 하는 칸의 개수의 최솟값 출력
    print(f"#{test_case} {N * M - max_color}")


# 실행 결과: 성공(메모리:57,736 kb, 시간:126 ms)
