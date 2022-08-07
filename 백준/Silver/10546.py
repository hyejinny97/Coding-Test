# https://www.acmicpc.net/problem/10546
# 문제10546번.배부른 마라토너
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 참가자 수 N
- 1 <= N <= 10^5
2. N개의 줄에 참가자의 이름
3. N - 1개의 줄에 완주한 참가자의 이름
- 1 <= 참가자 이름 <= 20
- 동명이인이 있을 수 있음
'''



# 출력
'''
1. 마라톤을 완주하지 못한 참가자의 이름 출력
'''



# 코드 1
from email.policy import default
import sys
from collections import Counter

sys.stdin = open('input_text/10546.txt')

# 참가자 기록
N = int(input())
participant = Counter(input() for _ in range(N))

# 완주한 사람 체크
for _ in range(N - 1):
    finish = input()
    participant[finish] -= 1

# 완주하지 못한 사람 출력
print(participant.most_common(1)[0][0])



# 실행 결과: input()대신 sys.stdin.readline()으로 했을 때, 성공(메모리:44720kb, 시간:248ms)



# 코드 2
import sys

sys.stdin = open('input_text/10546.txt')

# 참가자 기록
N = int(input())
same_name = {}   # 동명이인 명단
participant = set()   # 참가자 명단
for _ in range(N):
    person = input()
    # 참가자 명단에 없는 경우, 추가
    if person not in participant:
        participant.add(person)
    # 이미 참가자 명단에 있는 경우, 동명이인
    else:
        # 이미 동명이인 명단에 있는 경우
        if same_name.get(person):
            same_name[person] += 1
        # 동명이인 명단에 없는 경우
        else:
            same_name[person] = 2

# 완주한 사람 체크
for _ in range(N - 1):
    finish = input()
    # 동명이인 명단에 있는 경우
    if same_name.get(finish):
        same_name[finish] -= 1
        if same_name[finish] == 0:
            del same_name[finish]
            participant.remove(finish)
    # 동명이인 명단에 없는 경우
    else:
        participant.remove(finish)

# 완주하지 못한 사람 출력
print(*participant)



# 실행 결과: input()대신 sys.stdin.readline()으로 했을 때, 성공(메모리:42108kb, 시간:200ms)



# 코드 3
import sys

sys.stdin = open('input_text/10546.txt')

# 참가자 기록 및 완주자 체크
N = int(input())
participant = set()   # 참가자 명단
for _ in range(2 * N - 1):
    person = input()
    if person in participant:
        participant.remove(person)
    else:
        participant.add(person)

# 완주하지 못한 사람 출력
print(*participant)



# 실행 결과: input()대신 sys.stdin.readline()으로 했을 때, 성공(메모리:42108kb, 시간:224ms)