# https://www.acmicpc.net/problem/2775
# 문제2775번.부녀회장이 될테야
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스 T
2. T줄마다 첫째 줄에 층 수 k, 둘째 줄에 호 수 n
- 1 ≤ k, n ≤ 14
'''



# 출력
'''
1. T줄마다 해당 집에 거주민 수를 출력

<거주 조건>
- a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야 한다
- 아파트에는 0층부터 있음
- 각층에는 1호부터 있음
- 0층의 i호에는 i명이 살고 있음
'''



# 코드

# 접근 방법
'''
3층  1    1+1+(1+2)      1+1+(1+2)+1+(1+2)+(1+2+3)   
2층  1    1+(1+2)        1+(1+2)+(1+2+3)              1+(1+2)+(1+2+3)+(1+2+3+4)
1층  1    1+2            1+2+3                        1+2+3+4
0층  1    2              3                            4
     1호  2호            3호                          4호

- (3층, 4호) 거주민 수 = 1 x 4 + (1+2) x 3 + (1+2+3) x 2 + (1+2+3+4) x 1
                       
3층  1    5    15   35
2층  1    4    10   20
1층  1    3    6    10
0층  1    2    3    4
     1호  2호  3호  4호

- (k층, n호) 거주민 수 = (k-1층, n호) 거주민 수 + (k층, n-1호) 거주민 수

    0호  1호  2호  3호  4호
0층  0   1    2    3    4
1층  0   1    3    6    10
2층  0   1    4    10   20
3층  0   1    5    15   35
'''

import sys

sys.stdin = open('input_text/2775.txt')

# 14 x 14 배열에서 각 집마다 거주민 수 모두 구하기
apartment = [list(range(0, 14 + 1))]
for _ in range(14):
    apartment.append([0] * 15)

for r in range(1, 14 + 1):
    for c in range(1, 14 + 1):
        apartment[r][c] = apartment[r-1][c] + apartment[r][c-1]

# (k층, n호) 집의 거주민 수 구하기
T = int(input())
for _ in range(T):
    k = int(input())  # 층
    n = int(input())  # 호
    print(apartment[k][n])


# 실행 결과: 성공(메모리:31256kb, 시간:52ms)