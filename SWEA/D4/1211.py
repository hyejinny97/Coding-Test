# 문제1210번.Ladder2
# 시간: 30초, 메모리: 256MB



# 입력
'''
<10개의 테스트 케이스>
1. 테스트 케이스 번호
2. 100개의 각 줄에 2차원 배열의 각 행이 입력으로 주어짐
- 1: 사다리
- 0: 이외는 0으로 채워짐
- 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 존재
- 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 해야함
'''



# 출력
'''
1. #{테스트케이스} {최단거리로 바닥에 도착하게 되는 출발점의 x좌표}
'''



# 코드 1
import sys, copy

sys.stdin = open('../input_text/1211.txt')

def length_of_ladder(r, c) -> int:
    length = 1
    while True:
        # 도착점이면 사다리 길이 반환
        if r == 99:
            return length
        
        # 좌 우 아래 탐색
        dr = [0, 0, 1]   # 좌 우 아래
        dc = [-1, 1, 0]
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr < 100 and 0 <= nc < 100 and matrix[nr][nc] == '1':
                length += 1
                r, c = nr, nc
                matrix[nr][nc] = '0'   # 지나온 곳 체크
                break


# 사다리 2차원 배열 입력받기
T = 10
for _ in range(T):
    test_case = int(input())
    original = [input().split() for _ in range(100)]

    # 첫 행을 순회하면서 진입점 찾기
    tot_length_of_ladder = []
    for i in range(0, 99 + 1):
        matrix = copy.deepcopy(original)
        if matrix[0][i] == '1':
            tot_length_of_ladder.append((length_of_ladder(0, i), i))
    
    print(f'#{test_case} {min(tot_length_of_ladder)[1]}')



# 실행 결과: 실패((Runtime error)Memory error occured, (e.g. segmentation error, memory limit Exceed, stack overflow,... etc))



# 코드 2
import sys, copy

sys.stdin = open('../input_text/1211.txt')

def length_of_ladder(r, c) -> int:
    length = 1
    while True:
        # 도착점이면 사다리 길이 반환
        if r == 99:
            return length
        
        # 좌 우 탐색해서 이동가능하면 끝까지 이동
        dr = [0, 0]   # 좌 우
        dc = [-1, 1]
        moved = False   # 좌 우 중 한 방향으로 이동했는지 여부
        for i in range(2):
            while True:
                nr = r + dr[i]
                nc = c + dc[i]
                if nr < 100 and 0 <= nc < 100 and matrix[nr][nc] == '1':
                    length += 1
                    r, c = nr, nc
                    moved = True
                else:
                    break  
            # 좌로 이미 이동한경우, 우로 이동할 필요가 없음
            if moved:
                break

        # 아래로 한칸 이동
        r += 1


# 사다리 2차원 배열 입력받기
T = 10
for _ in range(T):
    test_case = int(input())
    matrix = [input().split() for _ in range(100)]

    # 첫 행을 순회하면서 진입점 찾기
    tot_length_of_ladder = []
    for i in range(0, 99 + 1):
        if matrix[0][i] == '1':
            tot_length_of_ladder.append((length_of_ladder(0, i), i))
    
    print(f'#{test_case} {min(tot_length_of_ladder)[1]}')



# 실행 결과: 성공(메모리:62,996 kb, 시간:238 ms)