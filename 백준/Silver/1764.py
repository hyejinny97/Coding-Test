# https://www.acmicpc.net/problem/1764
# 문제1764번.듣보잡
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 듣지도 못한 사람의 수 N, 보지도 못한 사람의 수 M
- 0 < N, M <= 500,000
2. N개의 줄에 듣지도 못한 사람의 이름
3. M개의 줄에 보지도 못한 사람의 이름
- 이름 길이 <= 20
- 중복 x
'''



# 출력
'''
1. 듣보잡 수, 명단을 사전 순으로 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1764.txt')

N, M = map(int, input().split())

# 듣지도 못한 사람 수 기록
noheard = set()
for _ in range(N):
    noheard.add(sys.stdin.readline())

# 보지도 못한 사람 수 기록
nosaw = set()
for _ in range(N):
    nosaw.add(sys.stdin.readline())

# 듣도 보도 못한 사람
nobody = noheard & nosaw
print(len(nobody))
print(''.join(sorted(nobody)))



# 실행 결과: 성공(메모리:42108kb, 시간:120ms)