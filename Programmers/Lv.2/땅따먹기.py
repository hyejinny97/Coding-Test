# https://school.programmers.co.kr/learn/courses/30/lessons/12913
# 코딩테스트연습 < 연습문제 < 문제.땅따먹기



# 입력
'''
1. N행 4열로 이루어진 땅 land
- 0 < N <= 100,000
- 모든 칸에는 점수가 쓰여 있음
- 점수 : 100 이하의 자연수
'''



# 출력
'''
1. 마지막 행까지 모두 내려왔을 때, 얻을 수 있는 점수의 최대값을 return

<게임 규칙>
- 1행부터 땅을 밟으며 한 행씩 내려올 때, 각 행의 4칸 중 한 칸만 밟으면서 내려와야함
- 한 행씩 내려올 때, 같은 열을 연속해서 밟을 수 없음
'''


# 코드 1

# 접근방법
'''
- 각 행의 각 칸에 올 수 있는 최댓값을 계속해서 구해나가기 (DP)
- 즉, 자신의 행 바로 위의 행에서 자신과 같은 열을 가진 점수를 제외한 나머지 3개의 열에서 최댓값과의 합이 본인 칸에서의 최댓값을 가지는 방법임
- 결국 각 칸은 가장 높은 점수를 받기 위해 최선의 길로만 이동한게 틀림없음
- 따라서, 본인 칸의 바로 위의 행을 제외하곤 다른 행을 볼 필요가 없음

land
1   2   3   5
5   6   7   8
1   2   100 3
      ↓
1   2   3   5
10  11  12  11
13  14  111 15
'''
import sys

sys.stdin = open('input_text/땅따먹기.txt')

def solution(land):
    for r in range(1, len(land)):
        land[r][0] += max(land[r-1][1], land[r-1][2], land[r-1][3])
        land[r][1] += max(land[r-1][2], land[r-1][3], land[r-1][0])
        land[r][2] += max(land[r-1][3], land[r-1][0], land[r-1][1])
        land[r][3] += max(land[r-1][0], land[r-1][1], land[r-1][2])
    
    return max(land[-1])


# 실행 결과: 성공



# 코드 2
import sys

sys.stdin = open('input_text/땅따먹기.txt')

def solution(land):
    for r in range(1, len(land)):
        for c in range(4):
            land[r][c] += max(land[r-1][:c] + land[r-1][c+1:])
    
    return max(land[-1])


# 실행 결과: 성공