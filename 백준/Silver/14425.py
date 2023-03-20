# https://www.acmicpc.net/problem/14425
# 문제14425번.문자열 집합
# 시간: 2초, 메모리: 1536MB



# 입력
'''
1. 문자열의 개수 N과 M
- 1 ≤ N ≤ 10,000
- 1 ≤ M ≤ 10,000
2. N개의 줄에는 집합 S에 포함되어 있는 문자열들
3. M개의 줄에는 검사해야 하는 문자열들
- 문자열은 알파벳 소문자로만 이루어짐
- 0 < 문자열 길이 <= 500
- 같은 문자열이 중복되는 경우는 없음
'''



# 출력
'''
1. M개의 문자열 중에 총 몇 개가 집합 S에 포함되어 있는지 출력
'''



# 코드
import sys

sys.stdin = open('input_text/14425.txt')

N, M = map(int, input().split())
words = set()

for _ in range(N):
    word = input()
    words.add(word)

cnt = 0
for _ in range(M):
    word = input()
    if word in words:
        cnt += 1

print(cnt)


# 실행 결과: 성공(메모리:36684kb, 시간:876ms)