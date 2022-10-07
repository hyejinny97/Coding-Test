# 문제8673번.코딩 토너먼트1
# 시간: 초, 메모리: 256MB


# 입력
"""
1. 테스트 케이스 수 T
2. 정수 K (= 경기의 수)
- 1 ≤ K ≤ 10
3. 2^K명의 코딩 실력
- 1 ≤ 코딩 실력 ≤ 100,000
"""


# 출력
"""
1. #{테스트케이스} {경기의 지루한 정도의 총합}
- 경기의 지루한 정도의 총합 = 실력이 차이의 총합
- 두 사람이 코딩 대결을 하면 코딩 실력이 높은 사람이 반드시 승자가 된다
- 만약 두 사람의 코딩 실력이 같으면 둘 중 한 명이 이긴다.
"""


# 코드
import sys

sys.stdin = open("../input_text/8673.txt")

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())
    skills = list(map(int, input().split()))   # 2^K명의 실력

    # 실력 차의 총합 구하기
    tot_diff = 0
    player = 2 ** K
    now = skills   # 현재 경기에서의 사람들
    winner = []   # 경기에서 우승한 사람들
    while player > 1:
        for i in range(0, player, 2):
            tot_diff += abs(now[i] - now[i + 1])
            winner.append(max(now[i], now[i + 1]))
        player //= 2
        now = winner
        winner = []

    print(f'#{test_case} {tot_diff}')


# 실행 결과: 성공(메모리:56,984 kb, 시간:114 ms)