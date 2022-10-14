# https://school.programmers.co.kr/learn/courses/30/lessons/42889
# 코딩테스트연습 < 2019 KAKAO BLIND RECRUITMENT < 문제.실패율



# 입력
'''
1. 전체 스테이지의 개수 N
- 1 <= N <= 500
2. 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages
- 1 <= 길이 <= 200,000
- 1 <= 번호 <= N + 1
- N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자
'''



# 출력
'''
1. 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return
- 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
- 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다
- 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의
'''



# 코드 1
import sys

sys.stdin = open('input_text/실패율.txt')

# stages: 인덱스 = i번째 사람, 값 = i번쨰 사람이 현재 위치한 스테이지 번호
def solution(N, stages):
    # 각 스테이지 당 몇 명이 있는지 
    stage_people = [0] * (N + 2)   # 인덱스 = 스테이지 번호, 값 = 몇 명
    for stage in stages:
        stage_people[stage] += 1

    # 뒤에서부터 누적
    acc_people = [0] * (N + 2)   
    acc = 0
    for i in range(N + 1, 0, -1):
        acc += stage_people[i]
        acc_people[i] = acc

    # 실패율 구하기
    fails = [0] * (N + 2)   
    for i in range(N + 1, 0, -1):
        if acc_people[i] == 0:
            continue
        fails[i] = (i, stage_people[i] / acc_people[i])
    
    # 실패율이 높은 스테이지부터 내림차순으로 스테이지 번호가 담겨있는 배열 출력
    order = sorted(fails[1 : N + 1], key=lambda x: (x[1], -x[0]), reverse=True)
    answer = []
    for o in order:
        answer.append(o[0])
    return answer
        

# 실행 결과: 실패(일부 문제 런타임 에러)



# 코드 2
import sys

sys.stdin = open('input_text/실패율.txt')

def solution(N, stages):
    answer = {}   # 키 = 스테이지 번호, 값 = 실패율
    remain = len(stages)   # 현재 번호 이후의 사람들 총합 = 스테이지에 도달한 플레이어 수
    for stage in range(1, N + 1):
        if remain > 0:
            now = stages.count(stage)   # 현재 스테이지에 존재하는 사람 수
            answer[stage] = now / remain
            remain -= now
        else:
            answer[stage] = 0
    
    return sorted(answer, key=lambda stage: answer[stage], reverse=True)


# 실행 결과: 성공