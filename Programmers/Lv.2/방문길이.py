# https://school.programmers.co.kr/learn/courses/30/lessons/49994
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.방문길이



# 입력
'''
1. 명령어 dirs
- string형으로 주어지며, 'U', 'D', 'R', 'L' 문자
- 0 < dirs 길이 <= 500
'''



# 출력
'''
1. 게임 캐릭터가 처음 걸어본 길의 길이를 구하여 return 
- 좌표평면: x = -5 ~ 5, y = -5 ~ 5
- 캐릭터는 좌표평면의 (0, 0) 위치에서 시작
- 명령어: U(위), D(아래), R(오른쪽), L(왼쪽) 
- 단, 좌표평면의 경계를 넘어가는 명령어는 무시

'''


# 코드 1

# 접근방법
'''
1. 좌표평면을 x = 0 ~ 10, y = 0 ~ 10 로 변경
2. 캐릭터는 (5, 5)에서 시작
3. x < 0 or y < 0 or x > 10 or y > 10으로 이동하는 명령어는 무시
4. 2차원 배열 좌표의 현재 위치(x, y)에서 어느 방향(dx, dy)으로 이동했는지 기록
- 수정) 어느 방향으로 이동했는지가 아니라 어느 '좌표'로 이동했는지 기록

ex) dirs = "ULURRDLLU"인 경우 👉 이동길이 = 7

     x
     0         1         2         3         4         5          6       ...
 y 0              
   1 
   2
   3
   4
   5                                                    [(0,1)]
   6                                         [(0,1)]    [(-1,0)]   [(-1,0)]   
   7                                         [(1,0)]    [(1,0)]    [(0,-1)]
   .
   .
   .
'''
import sys

sys.stdin = open('input_text/방문길이.txt')

def solution(dirs):
    # 10 x 10 크기의 좌표평면
    matrix = []
    for _ in range(11):
        row = []
        for _ in range(11):
            row.append([])
        matrix.append(row)
    
    # 명령어에 따라 이동할 때, 현재 위치에서 어느 '방향'으로 이동했는지 기록
    x, y = [5, 5]  # 캐릭터 현재 위치
    direction = {'R': (1, 0), 'L': (-1, 0), 'D': (0, -1), 'U': (0, 1)}
    distance = 0  # 처음 걸어본 길의 길이
    for d in dirs:
        # 좌표평면 경계를 벗어나는 경우, 명령어 무시
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:  
            continue
        
        # 이동 '방향' 기록
        if direction[d] not in matrix[x][y]:
            matrix[x][y].append(direction[d])
            distance += 1
        
        # 캐릭터 이동
        x, y = nx, ny 

    return distance


# 실행 결과: 실패(이유: 왼쪽 → 오른쪽으로 이동한 길과 오른쪽 → 왼쪽으로 이동한 길은 같기 때문)



# 코드 2

# 접근방법
'''
- 수정) 어느 '방향'으로 이동했는지가 아니라 어느 '좌표'로 이동했는지 기록
- 출발점에서 도착점 좌표를 기록할 뿐만 아니라, 도착점에서 출발점 좌표를 기록해야함
'''
import sys

sys.stdin = open('input_text/방문길이.txt')

def solution(dirs):
    # 10 x 10 크기의 좌표평면
    matrix = []
    for _ in range(11):
        row = []
        for _ in range(11):
            row.append([])
        matrix.append(row)
    
    # 명령어에 따라 이동할 때, 현재 위치에서 어느 '좌표'로 이동했는지 기록
    x, y = [5, 5]  # 캐릭터 현재 위치
    direction = {'R': (1, 0), 'L': (-1, 0), 'D': (0, -1), 'U': (0, 1)}
    distance = 0  # 처음 걸어본 길의 길이
    for d in dirs:
        # 좌표평면 경계를 벗어나는 경우, 명령어 무시
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if nx < 0 or ny < 0 or nx > 10 or ny > 10:  
            continue
        
        # 이동 '좌표' 기록
        if (nx, ny) not in matrix[x][y]:
            matrix[x][y].append((nx, ny))  # 출발점에서 이동 좌표 기록
            matrix[nx][ny].append((x, y))  # 도착점에서 이동 좌표 기록
            distance += 1
        
        # 캐릭터 이동
        x, y = nx, ny 

    return distance


# 실행 결과: 성공



# 코드 3
import sys

sys.stdin = open('input_text/방문길이.txt')

def solution(dirs):
    x, y = 0, 0  # 캐릭터 현재 위치
    direction = {'R': (1, 0), 'L': (-1, 0), 'D': (0, -1), 'U': (0, 1)}
    record = set()  # 캐릭터가 이동한 길
    for d in dirs:
        # 좌표평면 경계를 벗어나는 경우, 명령어 무시
        nx = x + direction[d][0]
        ny = y + direction[d][1]
        if nx < -5 or ny < -5 or nx > 5 or ny > 5:  
            continue
        
        # 이동 '좌표' 기록
        record.add((x, y, nx, ny))  # 출발점 → 도착점
        record.add((nx, ny, x, y))  # 도착점 → 출발점

        # 캐릭터 이동
        x, y = nx, ny 

    return len(record) // 2


# 실행 결과: 성공