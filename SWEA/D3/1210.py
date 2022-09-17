# 문제1210번.Ladder1
# 시간: 30초, 메모리: 256MB



# 입력
'''
<10개의 테스트 케이스>
1. 테스트 케이스 번호
2. 100개의 각 줄에 2차원 배열의 각 행이 입력으로 주어짐
- 1: 사다리
- 2: 도착 지점
- 0: 이외는 0으로 채워짐
- 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 존재
- 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 해야함
'''



# 출력
'''
1. #{테스트케이스} {도착하게 되는 출발점의 x좌표}
'''



# 코드 1 - 사다리 위에서 아래로 훑기
import sys

sys.stdin = open('../input_text/1210.txt')

# 지정된 도착점에 도착하는 사다리인지 확인
def ladder(r, c) -> bool:
    while True:
        # 현재 노드가 마지막 행에 도착한 경우
        if r == 99:
            # 지정된 도착지점에 도착한 경우
            if matrix[r][c] == '2':
                return True
            return False
                
        # 좌우 탐색한 후, 좌우로 이동가능하면 끝까지 이동
        dc = [1, -1]    # 좌 우
        for i in range(2):
            moved = False   # 좌우로 이동했는지 여부
            while True:
                nc = c + dc[i]
                if 0 <= nc < 100 and matrix[r][nc] == '1':
                    c = nc
                    moved = True
                else:
                    break
            # 좌로 이동한 경우, 우로 다시 이동할 필요 없음
            if moved:
                break
        # 아래로 이동
        r += 1


T = 10
for _ in range(T):
    test_case = int(input())
    matrix = [input().split() for _ in range(100)]

    # 2차원 배열을 첫번째 행을 순회
    for i in range(100):
        # 진입점(1인 곳) 찾기
        if matrix[0][i] == '1':
            # 지정된 도착점에 도착하게 되는 출발점인 경우
            if ladder(0, i):
                print(f'#{test_case} {i}')
                break



# 실행 결과: 성공(메모리:63,256 kb, 시간:202 ms)



# 코드 2 - 도착 지점에서 출발해서 출발점을 거꾸로 유추
import sys

sys.stdin = open('../input_text/1210.txt')

# 도착점에서 위로 거슬러 올라가서 출발점 찾기
def ladder(r, c) -> int:
    while r != 0:
        # 좌 우 위순으로 탐색
        dr = [0, 0, -1]   # 좌 우 위
        dc = [1, -1, 0]   
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr and 0 <= nc < 100 and matrix[nr][nc] == '1':
                r, c = nr, nc
                matrix[nr][nc] = '0'   # 지나온 곳 체크
                break   
    return c


T = 10
for _ in range(T):
    test_case = int(input())
    matrix = [input().split() for _ in range(100)]

    # 도착 지점에서 출발
    for i in range(100):
        # 도착점(2인 곳) 찾기
        if matrix[99][i] == '2':
            print(f'#{test_case} {ladder(99, i)}')
            break



# 실행 결과: 성공(메모리:62,264 kb, 시간:194 ms)