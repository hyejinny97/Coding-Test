# https://school.programmers.co.kr/learn/courses/30/lessons/42840?language=python3
# 코딩테스트연습 < 완전 탐색 < 문제.모의고사



# 입력
'''
1. 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers
- 0 < 시험 문제 수 <= 10,000
'''



# 출력
'''
1. 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
- 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬
'''



# 코드
import sys

sys.stdin = open('input_text/모의고사.txt')

def solution(answers):
    fst = [1, 2, 3, 4, 5]   # 1번 수포자
    sec = [2, 1, 2, 3, 2, 4, 2, 5]   # 2번 수포자
    thd = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # 3번 수포자

    # 문제의 정답을 순회
    scores = [0] * 4   # 인덱스:1~3번 수포자, 값:점수
    for num in range(len(answers)):   # 현재 정답 비교하는 문제의 번호
        if fst[num % len(fst)] == answers[num]:
            scores[1] += 1
        if sec[num % len(sec)] == answers[num]:
            scores[2] += 1
        if thd[num % len(thd)] == answers[num]:
            scores[3] += 1

    # 가장 높은 점수를 받은 사람 확인
    max_score = max(scores)
    top_rank = [i for i in range(1, 3 + 1) if scores[i] == max_score]   # 가장 높은 점수를 받은 사람

    return sorted(top_rank)
        

# 실행 결과: 성공