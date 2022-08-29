# https://www.acmicpc.net/problem/2477
# 문제2477번.참외밭
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 1m2의 넓이에 자라는 참외의 개수 K
- 1 <= K <= 20
2. 6개의 줄에 변의 방향과 길이
- 참외밭을 나타내는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계방향으로 둘레를 돌면서 지나는 변의 방향과 길이
- 변의 방향: 동쪽(1), 서쪽(2), 남쪽(3), 북쪽(4)
- 1 <= 변의 길이 <= 500
'''



# 출력
'''
1. 주어진 밭에서 자라는 참외의 수를 출력
- 1m2의 넓이에 자라는 참외 개수를 헤아린 다음, 참외밭의 넓이를 구하면 비례식을 이용하여 참외의 총개수를 구할 수 있음
'''



# 코드
import sys

sys.stdin = open('input_text/2477.txt')

# 6개의 변의 길이와 방향 입력 받기
K = int(input())   # 1m2의 넓이에 자라는 참외의 개수
sides = []   # 값: (변의 방향, 변의 길이)
dirs_cnt = [0] * 5   # 인덱스: 1~4방향, 값: 등장 횟수
dir_val = [[] for _ in range(5)]   # 인덱스: 1~4방향, 값: 변의 길이
for _ in range(6):
    dir, l = map(int, input().split())
    sides.append((dir, l))
    dirs_cnt[dir] += 1
    dir_val[dir].append(l)

# 가장 긴 길이의 두 변을 찾아 큰 사각형의 넓이 구하기
large_sq = 1   # 큰 사각형의 넓이
large_l = []
for dir in range(1, 4 + 1):
    if dirs_cnt[dir] == 1:
        large_sq *= dir_val[dir][0]
        large_l.append(dir)

# 작은 사각형의 넓이 구하기
small_sq = 1   # 작은 사각형의 넓이
for i in range(6):
    if sides[i][0] in large_l:
        small_sq *= sides[i - 3][1]

print((large_sq - small_sq) * K)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)