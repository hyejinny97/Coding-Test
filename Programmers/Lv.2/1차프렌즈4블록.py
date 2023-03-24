# https://school.programmers.co.kr/learn/courses/30/lessons/17679
# 코딩테스트연습 < 2018 KAKAO BLIND RECRUITMENT < 문제.[1차] 프렌즈4블록



# 입력
'''
1. 판의 높이 m, 폭 n
- 2 ≦ n, m ≦ 30
2. 판의 배치 정보 board
- board는 길이 n인 문자열 m개의 배열
- 블록을 나타내는 문자: 대문자 A-Z
'''



# 출력
'''
1. 판 정보를 가지고 몇 개의 블록이 지워질지 출력
- 록이 2x2 형태로 4개가 붙어있을 경우 사라짐
- 2x2 모양이 여러 개 있다면 한꺼번에 지워짐
- 블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 되는데, 빈 공간을 채운 후에 다시 2x2 형태로 같은 모양의 블록이 모이면 다시 지워짐
'''



# 코드 

# 접근방법
'''
1. board 전체를 반복문으로 돌면서, 방향벡터를 사용해 2x2 모양이 있는지 확인    
2. 2x2 모양(4블록)을 발견한 경우
   - go_next = True
   - 4블록에 해당하는 블록 개수 카운트
   - 해당 블록들을 True로 변환
   - 블록을 아래로 떨어뜨리기 👉 각 column을 위에서 아래로 확인하면서 True 블록을 위로 끌어올리기
3. go_next = True이면, 1번으로 다시 돌아감
4. go_next = False이면, 반복을 종료

<board 초기배치>
TTTANT
RRFACC
RRRFCC
TRRRAA
TTMMMF
TMMTTJ
   ↓ 1-2번) cnt = 11, go_next = True
TTTANT
..FA..
...F..
T..RAA
TTMMMF
TMMTTJ
   ↓
...A..
...A..
T.TFNT
TTFRAA
TTMMMF
TMMTTJ   
   ↓ 3번, 1-2번) cnt = 15, go_next = True
...A..
...A..
T.TFNT
..FRAA
..MMMF
TMMTTJ 
   ↓ 
...A..
...A..
..TFNT
..FRAA
T.MMMF
TMMTTJ 
   ↓ 3번, 1-2번) cnt = 15, go_next = False
   ↓ 4번
반복 종료
'''
import sys

sys.stdin = open('input_text/1차프렌즈4블록.txt')

# 2x2 모양(4블록) 확인하고 지우기 (지운 블록 개수를 반환)
def find_4block(board: list, check_board: list) -> int: 
    remove_block_cnt = 0   # 지운 블록 개수
    for r in range(len(board) - 2 + 1):
        for c in range(len(board[0]) - 2 + 1):
            same_block_cnt = 0  # 2x2 범위 내에 자신의 블록과 동일한 블록 갯수
            
            # 방향벡터 (dr, dc)을 사용해 2x2 범위 내 블록 확인
            directions = [(0, 0), (0, 1), (1, 0), (1, 1)]  # 현재, 동, 남, 남동
            for d in directions:
                nr = r + d[0]
                nc = c + d[1]
                if board[r][c] and board[r][c] == board[nr][nc]:
                    same_block_cnt += 1
            
            # 4블록을 만족하면, 카운트하고 해당 블록 지우기
            if same_block_cnt == 4:
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if not check_board[nr][nc]:
                        remove_block_cnt += 1
                    check_board[nr][nc] = True
            
    return remove_block_cnt


# 블록을 아래로 떨어뜨리기
def move_blocks(board: list, check_board: list) -> None:
    # board의 행렬을 바꾼 후, 지워지지 않은 블록만 새로 담기
    new_board = []
    for c in range(len(board[0])):
        row = []
        for r in range(len(board) - 1, 0 - 1, -1):
            if not check_board[r][c]:
                row.append(board[r][c])
        row += [0] * (len(board) - len(row))
        new_board.append(row)
    
    # board의 행렬을 다시 원래대로 돌려놓기
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c] = new_board[c][len(board) - r - 1]
              

def solution(m, n, board):
    board = [list(board[r]) for r in range(m)]
    go_next = True   # 다음 스텝 진행 여부
    tot_remove_block_cnt = 0   # 지워진 블록 총 개수
    while go_next:
        check_board = [[False] * n for _ in range(m)]

        # 2x2 모양(4블록) 확인하고 지우기
        remove_block_cnt = find_4block(board, check_board)
        tot_remove_block_cnt += remove_block_cnt
        go_next = bool(remove_block_cnt)

        # 블록을 아래로 떨어뜨리기
        move_blocks(board, check_board)
        
    return tot_remove_block_cnt


# 실행 결과: 성공