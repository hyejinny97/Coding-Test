# https://www.acmicpc.net/problem/7785
# 문제7785번.회사에 있는 사람
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 로그에 기록된 출입 기록의 수 n
- 2 <= n <= 1,000,000
2. 사람의 이름, 'enter' 또는 'leave'
- 동명이인은 없음
- 대소문자가 다른 경우, 다른 사람임
'''



# 출력
'''
1. 현재 회사에 있는 사람의 이름을 사전순의 역순으로 한줄에 한명씩 출력
'''



# 코드
import sys

sys.stdin = open('input_text/7785.txt')

N = int(input())
logs = {}   # 키:이름, 값: 출근/퇴근

# 딕셔너리에 출퇴근 기록 저장
for _ in range(N):
    name, log = input().split()
    logs[name] = log

# 현재 회사에 남아있는 사람들 
enters = []
for name in logs:
    if logs[name] == 'enter':
        enters.append(name)

# 이름의 역순으로 출력
enters.sort(reverse=True)
print('\n'.join(enters))



# 실행 결과: 성공(메모리:49724kb, 시간:3984ms)