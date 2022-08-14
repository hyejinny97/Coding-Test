# https://www.acmicpc.net/problem/14467
# 문제14467번.소가 길을 건너간 이유1
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 관찰 횟수 N
- 0 < N <= 100
2. N개의 줄에 소의 번호, 위치(0 또는 1)
'''



# 출력
'''
1. 소가 길을 건너간 최소 횟수 출력
- 총 소 10마리
'''



# 코드 
import sys

sys.stdin = open('input_text/14467.txt')

N = int(input())

cows_loc = ['.'] * (10 + 1)   # 인덱스: 1 ~ 10번 소, 값: 소의 위치
cnt = 0   # 소가 길을 건너간 최소 횟수
for _ in range(N):
    cow, loc = map(int, input().split())
    if cows_loc[cow] == '.':
        cows_loc[cow] = loc
    elif cows_loc[cow] != loc:
        cnt += 1
        cows_loc[cow] = loc

print(cnt)



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)