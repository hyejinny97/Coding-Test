# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 코딩테스트연습 < 연습문제 < 문제.달리기 경주



# 입력
'''
1. 선수들의 이름이 1등부터 현재 등수 순서대로 담긴 문자열 배열 players
- 5 ≤ players의 길이 ≤ 50,000
- 3 ≤ players[i]의 길이 ≤ 10
2. 해설진이 부른 이름을 담은 문자열 배열 callings
- 2 ≤ callings의 길이 ≤ 1,000,000
- callings는 players의 원소들로만 이루어져 있음
- 경주 진행중 1등인 선수의 이름은 불리지 않음
'''



# 출력
'''
1. 경주가 끝났을 때 선수들의 이름을 1등부터 등수 순서대로 배열에 담아 return
- 해설진들은 선수들이 자기 바로 앞의 선수를 추월할 때 추월한 선수의 이름을 부름
'''



# 코드 1
import sys

sys.stdin = open('input_text/달리기경주.txt')

def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players.remove(call)
        players.insert(idx - 1, call)

    return players


# 실행 결과: 실패(시간초과)



# 코드 2
import sys

sys.stdin = open('input_text/달리기경주.txt')

def solution(players, callings):
    for call in callings:
        idx = players.index(call)
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

    return players


# 실행 결과: 실패(시간초과)



# 코드 3
import sys

sys.stdin = open('input_text/달리기경주.txt')

def solution(players, callings):
    player_loc = dict((players[i], i) for i in range(len(players)))
    for call in callings:
        idx = player_loc[call]
        prev_player = players[idx - 1]
        players[idx - 1], players[idx] = players[idx], players[idx - 1]

        player_loc[prev_player] += 1
        player_loc[call] -= 1

    return players


# 실행 결과: 성공