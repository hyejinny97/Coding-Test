# 문제1285.아름이의 돌 던지기
# 시간: ?초, 메모리: 256MB

# 입력
'''
1. 테스트 케이스 총 개수 T
2. 돌을 던지는 사람의 수 N
- 1 <= N <= 100
3. N명의 사람이 돌을 던졌을 때, 돌이 떨어진 위치
- -100,000 <= 위치 <= 100,000
'''

# 출력
'''
1. #테스트케이스
2. 돌이 가장 0에 가깝게 떨어진 곳과 0 사이의 거리 차이
3. 그렇게 던진 사람이 몇 명인지
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/1285.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 각 사람마다 돌이 떨어진 위치와 0 사이의 거리 구하기
    diffs = map(lambda x: abs(int(x)), input().split())

    min_distance = 200000   # 100,000위치에서 -100,000위치로 돌을 던지는 경우로 초기화
    people = 0   # 0과의 차이가 최소가 되도록 던진 사람의 수
    for diff in diffs:
        # 거리차이가 더 작은 값이 나올때마다 갱신
        if min_distance > diff:
            min_distance = diff
            people = 1
        # 현재 최솟값과 거리차이가 동일한 경우 1씩 카운트
        elif min_distance == diff:
            people += 1
    
    print(f'#{test_case} {min_distance} {people}')
