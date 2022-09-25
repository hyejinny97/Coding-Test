# 문제14413번.격자판 칠하기
# 시간: 3초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 수 T
2. 격자판 크기 N x M
- 1 <= N, M <= 50
3. N개의 줄에 '#', '.', '?'로만 구성된 길이가 M인 문자열
'''



# 출력
'''
1. #{테스트케이스} {격자판의 인접한 두 칸의 색이 항상 서로 다르게 할 수 있다면 ‘possible’을, 그렇지 않다면 ‘impossible’을 출력}
- #: 검은색
- .: 흰색
- ?: 검은색 또는 흰색
'''


 
# 코드 1 - 위아래 인접한 변은 고려하지 않음
import sys

sys.stdin = open('../input_text/14413.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x M 크기의 배열 입력받기
    array = [input() for _ in range(N)]

    # 2차원 배열 순회하면서 색칠하기
    result = 'possible'
    for r in range(N):
        color = array[r][0]   # 현재 칸의 색깔
        for c in range(1, M):
            # 직전 칸의 색깔과 현재 칸의 색깔이 같은 경우
            if color == array[r][c] and array[r][c] != '?':
                result = 'impossible'
                break
            color = array[r][c]
        # 불필요한 순회 방지
        if result == 'impossible':
            break
    
    print(f'#{test_case} {result}')
                


# 실행 결과: 실패(73개의 테스트케이스 중 59개 통과)



# 코드 2
import sys

sys.stdin = open('../input_text/14413.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x M 크기의 배열 입력받기
    array = [input() for _ in range(N)]

    # 2차원 배열 순회하면서 색칠하기
    result = 'possible'
    for r in range(N):
        # 첫번째 열의 위아래 칸 비교
        if r > 0 and array[r][0] == array[r - 1][0] and array[r][0] != '?':
            result = 'impossible'
            break
        for c in range(1, M):
            # 직전 칸의 색깔과 현재 칸의 색깔이 같은 경우
            if array[r][c] == array[r][c - 1] and array[r][c] != '?':
                result = 'impossible'
                break
            # 바로 위 칸의 색깔과 현재 칸의 색깔이 같은 경우
            if r > 0 and array[r][c] == array[r - 1][c] and array[r][c] != '?':
                result = 'impossible'
                break
        # 불필요한 순회 방지
        if result == 'impossible':
            break
    
    print(f'#{test_case} {result}')
                


# 실행 결과: 실패(73개의 테스트케이스 중 66개 통과)



# 코드 3 - 완전히 다른 방식으로 접근
import sys

sys.stdin = open('../input_text/14413.txt')

# 행+열 인덱스 합이 짝수인 곳은 모두 #, 홀수인 곳은 모두 .인 경우 (?는 무시)
def start_black(array) -> bool:
    N, M = len(array), len(array[0])
    for r in range(N):
        for c in range(M):
            # 현재 색깔이 '?'인 경우 넘어가기
            if array[r][c] == '?':
                continue
            # 행 + 열 인덱스 합이 짝수인 칸
            if (r + c) % 2 == 0 and array[r][c] != '#':
                return False
            # 행 + 열 인덱스 합이 홀수인 칸
            elif (r + c) % 2 == 1 and array[r][c] != '.':
                return False
    return True

# 행+열 인덱스 합이 짝수인 곳은 모두 ., 홀수인 곳은 모두 #인 경우 (?는 무시)
def start_white(array) -> bool:
    N, M = len(array), len(array[0])
    for r in range(N):
        for c in range(M):
            # 현재 색깔이 '?'인 경우 넘어가기
            if array[r][c] == '?':
                continue
            # 행 + 열 인덱스 합이 짝수인 칸
            if (r + c) % 2 == 0 and array[r][c] != '.':
                return False
            # 행 + 열 인덱스 합이 홀수인 칸
            elif (r + c) % 2 == 1 and array[r][c] != '#':
                return False
    return True



T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x M 크기의 배열 입력받기
    array = [input() for _ in range(N)]

    # 2차원 배열 순회하면서 색칠하기
    if start_black(array) or start_white(array):
        result = 'possible'
    else:
        result = 'impossible'
    
    print(f'#{test_case} {result}')
                


# 실행 결과: 성공(메모리:61,948 kb, 시간:187 ms)



# 코드 4 - 코드 3을 리팩토링
import sys

sys.stdin = open('../input_text/14413.txt')

# 행+열 인덱스 합이 짝수인 곳은 모두 #, 홀수인 곳은 모두 .인 경우 (?는 무시)
# 행+열 인덱스 합이 짝수인 곳은 모두 ., 홀수인 곳은 모두 #인 경우 (?는 무시)
def match(even, odd) -> bool:
    N, M = len(array), len(array[0])
    for r in range(N):
        for c in range(M):
            # 현재 색깔이 '?'인 경우 넘어가기
            if array[r][c] == '?':
                continue
            # 행 + 열 인덱스 합이 짝수인 칸
            if (r + c) % 2 == 0 and array[r][c] != even:
                return False
            # 행 + 열 인덱스 합이 홀수인 칸
            elif (r + c) % 2 == 1 and array[r][c] != odd:
                return False
    return True


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    # N x M 크기의 배열 입력받기
    array = [input() for _ in range(N)]

    # 2차원 배열 순회하면서 색칠하기
    if match('#', '.') or match('.', '#'):
        result = 'possible'
    else:
        result = 'impossible'
    
    print(f'#{test_case} {result}')
                


# 실행 결과: 성공(메모리:61,944 kb, 시간:183 ms)