# https://www.acmicpc.net/problem/2116
# 문제2116번.주사위 쌓기
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 주사위의 갯수
- 0 < 갯수 <= 10,000
2. 한 줄에 하나씩 주사위의 각 면에 적혀 적혀진 숫자 6개
- 주사위의 전개도에서 A,B,C,D,E,F의 순서로 입력됨
- 종류가 같은 주사위도 있을 수 있음
- 보통 주사위처럼 마주보는 면에 적혀진 숫자의 합이 반드시 7이 되는 것은 아님
'''



# 출력
'''
1. 주사위 사각 기둥에서 한 옆면의 숫자의 합이 가장 큰 합을 출력
<주사위 쌓는 규칙>
- 서로 붙어 있는 두 개의 주사위에서 아래에 있는 주사위의 윗면에 적혀있는 숫자는 위에 있는 주사위의 아랫면에 적혀있는 숫자와 같아야 함
'''



# 코드
import sys

sys.stdin = open('input_text/2116.txt')

# 주사위 맞은 편 인덱스 짝지어 주기 
# ex) 0번 인덱스와 5번 인덱스는 맞은편에 위치
pair = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}

# 주사위 N개의 입력값 받기
N = int(input())
dices = [list(map(int, input().split())) for _ in range(N)]

# 옆면의 숫자 합 최댓값 찾기
# 1번 주사위 아래 값에 따라 이후의 주사위 쌓는 방법이 정해짐
max_sum = 0
for start_val in dices[0]:   # 1번 주사위
    floor = start_val   # 1번 주사위 아랫값 초기화
    sum_val = 0
    for j in range(N):   # N개의 주사위
        floor_idx = dices[j].index(floor)
        ceil = dices[j][pair[floor_idx]]    # 주사위 위값
        sum_val += max(set(range(1, 6 + 1)) - {floor, ceil})

        # 다음 주사위 아랫값 갱신
        floor = ceil
   
    # 숫자 합 최댓값 갱신
    max_sum = max(max_sum, sum_val)

print(max_sum)



# 실행 결과: 성공(메모리:31860kb, 시간:644ms)