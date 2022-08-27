# https://www.acmicpc.net/problem/2578
# 문제2578번.빙고
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 5개 줄에 빙고판에 쓰여진 수 5개
- 1부터 25까지의 수
2. 5개 줄에 사회자가 부르는 수 5개
'''



# 출력
'''
1. 사회자가 몇 번째 수를 부른 후 철수가 "빙고"를 외치게 되는지 출력
- 가로, 세로, 대각선이 세 개 이상 그어지면 "빙고"를 외침
'''



# 코드
import sys
from pprint import pprint

sys.stdin = open('input_text/2578.txt')

# 빙고판 번호를 입력받아 숫자를 기준으로 정렬하기
nums = [[0]]   # [숫자, r, c]
for r in range(1, 5 + 1):
    tmp = list(map(int, input().split()))
    for i in range(5):
        nums.append([tmp[i], r, i + 1])
nums.sort(key=lambda x: x[0])

# 사회자가 부르는 숫자에 따라 체크
bingo_r = [0] * 6   # 인덱스: 1번~5번 가로줄, 값: 체크 갯수
bingo_c = [0] * 6   # 인덱스: 1번~5번 세로줄, 값: 체크 갯수
diagonal_up = {(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)}   # 우상향 대각선의 (r,c) 값
diagonal_down = {(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}   # 우하향 대각선의 (r,c) 값
up_cnt, down_cnt = 0, 0   # 우상향/우하향 대각선 체크 갯수
check = 0   # 선을 긋는 횟수 (3개면 빙고)
say_num_cnt = 0   # 사회자가 부르는 숫자 갯수 카운트
for _ in range(5):
    say = list(map(int, input().split()))   # 사회자가 부르는 숫자 5개
    for say_num in say:
        say_num_cnt += 1
        r = nums[say_num][1]
        c = nums[say_num][2]

        # 가로/세로 체크
        bingo_r[r] += 1
        bingo_c[c] += 1
        if bingo_r[r] == 5:
            check += 1
        if bingo_c[c] == 5:
            check += 1

        # 대각선 체크
        if (r, c) in diagonal_up:
            up_cnt += 1
        if (r, c) in diagonal_down:
            down_cnt += 1
        if up_cnt == 5: 
            check += 1
            up_cnt = None
        if down_cnt == 5: 
            check += 1
            down_cnt = None

        # 빙고인지 확인
        if check >= 3:
            print(say_num_cnt)
            break
    
    # 불필요한 반복 방지
    if check >= 3:
        break



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)