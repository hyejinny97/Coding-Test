# https://www.acmicpc.net/problem/1931
# 문제1931번.회의실 배정
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 회의의 수 N
- 1 ≤ N ≤ 100,000
2. N 개의 줄마다 각 회의의 정보 (회의 시작 시간, 끝나는 시간)
- 0 <= 시간 <= 2^31 - 1
'''



# 출력
'''
1. 최대 사용할 수 있는 회의의 최대 개수를 출력
'''



# 코드

# 접근방법
'''
회의 끝나는 시간이 증가하는 순으로 확인하면서 
이전 회의 끝나는 시간과 현재 확인하고 있는 회의 시작 시간이
겹치지 않으면 선택

회의 끝나는 시간이 같으면 회의 시작 시간이 빠른 순으로 정렬
이유 ↓ 
3
4 4
4 4
1 4
'''
import sys

sys.stdin = open('input_text/1931.txt')

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))

selected = [meetings[0]]   # 선택된 회의들
cnt = 1  # 가능한 회의 개수
for i in range(1, N):
    if meetings[i][0] >= selected[-1][1]:
        cnt += 1
        selected.append(meetings[i])

print(cnt)


# 실행 결과: 성공(메모리:59204kb, 시간:268ms)