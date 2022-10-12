# https://school.programmers.co.kr/learn/courses/30/lessons/64061
# 코딩테스트연습 < 2019 카카오 개발자 겨울 인턴십 < 문제.크레인 인형뽑기 게임



# 입력
'''
1. 게임 화면의 격자의 상태가 담긴 2차원 배열 board
- 5 x 5 <= 2차원 배열 크기 <= 30 x 30
- 0 <= 각 칸 내 정수 <= 100
- 0: 빈 칸
- 1~100: 각기 다른 인형의 모양
2. 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves
- 1 <= 배열 크기 <= 1,000
- 1 <= 원소 <= board 배열의 가로 크기
'''



# 출력
'''
1. 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 
'''


# 코드 
import sys

sys.stdin = open('input_text/크레인인형뽑기게임.txt')

def solution(board, moves):
    # 차례대로 인형을 집어서 바구니에 옮겨 담기
    array = []   # 바구니에 넣어진 인형들
    dolls = 0   # 터트려져 사라진 인형의 개수
    for move in moves:
        for row in board:
            # 크레인을 내렸을 때, 인형이 있는 경우
            if row[move - 1]:
                # 바구니의 마지막과 일치하면 터트리기
                if array and array[-1] == row[move - 1]:
                    array.pop()
                    dolls += 2
                else:
                    array.append(row[move - 1])
                row[move - 1] = 0
                break

    return dolls


# 실행 결과: 성공