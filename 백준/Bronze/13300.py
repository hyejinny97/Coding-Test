# https://www.acmicpc.net/problem/13300
# 문제13300번.방 배정
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 수학여행에 참가하는 학생 수 N, 한 방에 배정할 수 있는 최대 인원수 K
- 1 <= N <= 1,000
- 1 < K <= 1,000
2. N개 줄에 학생의 성별 S, 학년 Y
- 1 <= Y <= 6
- S: 0은 여학생, 1은 남학생
'''



# 출력
'''
1. 학생들을 모두 배정하기 위해 필요한 최소한의 방의 수 출력
- 같은 성별끼리, 같은 학년끼리 한 방에 K명씩 배정해야함
'''



# 코드 
import sys

sys.stdin = open('input_text/13300.txt')

# 성별 학년별 리스트
boy = [0] * 7   # 인덱스: 1~6학년, 값: 각 학년별 남학생 수
girl = [0] * 7   # 인덱스: 1~6학년, 값: 각 학년별 여학생 수

# 학생 정보 입력 받기
N, K = map(int, input().split())
for _ in range(N):
    S, Y = map(int, input().split())
    
    if S == 0:   # 여학생
        girl[Y] += 1
    else:   # 남학생
        boy[Y] += 1

# 필요한 최소한의 방의 수 구하기
tot_cnt = 0
for i in range(1, 6 + 1):
    tot_cnt += boy[i] // K + 1 if boy[i] % K else boy[i] // K
    tot_cnt += girl[i] // K + 1 if girl[i] % K else girl[i] // K

print(tot_cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:120ms)