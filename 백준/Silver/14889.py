# https://www.acmicpc.net/problem/14889
# 문제14889번.스타트와 링크
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 축구를 하기 위해 모인 사람 N명
- 4 ≤ N ≤ 20
- N은 짝수
2. N개의 줄에 N개의 수
- Sij: (i번 줄의 j번째 수) i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치 
- Sii는 항상 0
- 1 <= Sij <= 100
'''



# 출력
'''
1. N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠, 두 팀의 능력치의 차이의 최솟값을 출력
- 팀의 능력치 =  Sij + Sji
- Sij는 Sji와 다를 수도 있음
'''



# 코드 1
import sys
from itertools import combinations

sys.stdin = open('input_text/14889.txt')

def make_team(team1=[], team1_power=0):  # 조합
    global min_team_power

    if len(team1) == N // 2:
        team2 = set(range(N)) - set(team1)
        team2_power = 0
        two_members = combinations(team2, 2)
        for two_member in two_members:
            fst, sec = two_member
            team2_power += powers[fst][sec] + powers[sec][fst]
        min_team_power = min(min_team_power, abs(team1_power - team2_power))
        return 

    for cur_member in range(N):
        if team1 and cur_member <= team1[-1]:
            continue
        
        # 기존 멤버와의 현재 멤버의 능력치 더하기
        new_team1_power = team1_power
        for prev_member in team1:
            new_team1_power += powers[prev_member][cur_member] + powers[cur_member][prev_member]

        make_team(team1 + [cur_member], new_team1_power)


N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

# N/2명의 팀으로 각각 나눠, 두 팀의 능력치의 차이 계산
min_team_power = 100 * 10 * 10   # 두 팀의 능력치의 차이의 최솟값
make_team()

print(min_team_power)


# 실행 결과: 성공(메모리:31256kb, 시간:2240ms)



# 코드 2

# 접근방법
'''
- 조합(combinations)을 이용해 팀을 나눔
- 순열(permutations)을 이용해 팀 내 선수들의 능력치를 합함 
'''
import sys
from itertools import combinations, permutations

sys.stdin = open('input_text/14889.txt')

N = int(input())
powers = [list(map(int, input().split())) for _ in range(N)]

# 두 팀으로 멤버 나누기 (조합)
possible_team1 = combinations(range(N), N // 2)
possible_team_members = []  
for team1 in possible_team1:
    team2 = set(range(N)) - set(team1)
    possible_team_members.append([team1, team2])

# 두 팀의 능력치의 차이 계산
min_team_power = 100 * 10 * 10   # 두 팀의 능력치의 차이의 최솟값
for teams in possible_team_members:
    team1, team2 = teams
    team1_power = sum(powers[mem1][mem2] for mem1, mem2 in permutations(team1, 2))
    team2_power = sum(powers[mem1][mem2] for mem1, mem2 in permutations(team2, 2))
    min_team_power = min(min_team_power, abs(team1_power - team2_power))

print(min_team_power)


# 실행 결과: 성공(메모리:208968kb, 시간:3188ms)