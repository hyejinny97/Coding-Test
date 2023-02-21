# https://www.acmicpc.net/problem/25305
# 문제25304번.커트라인
# 시간: 1초, 메모리: 1024MB



# 입력
'''
1. 응시자의 수 N, 상을 받는 사람의 수 k
- 1 <= N <= 1,000
- 1 <= k <= N
2. 각 학생의 점수 x
- 0 <= x <= 10,000
'''



# 출력
'''
1. 이들 점수 중 가장 높은 k명이 상을 받을 때, 상을 받는 커트라인이 몇 점인지 출력
- 커트라인: 상을 받는 사람들 중 점수가 가장 가장 낮은 사람의 점수
'''



# 코드
import sys

sys.stdin = open('input_text/25305.txt')

N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True)
print(scores[k - 1])


# 실행 결과: 성공(메모리:31256kb, 시간:56ms)