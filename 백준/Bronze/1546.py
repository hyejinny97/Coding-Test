# https://www.acmicpc.net/problem/1546
# 문제1546번.평균
# 시간제한:2초, 메모리제한:128MB



# 입력
'''
1. 시험 본 과목의 개수 N
- 0 < N <= 1,000
2. 세준이의 현재 성적
- 0 <= 성적 <= 100
'''



# 출력
'''
1. 새로운 평균을 출력

<새로운 평균을 구하는 방법>
- 자기 점수 중에 최댓값을 고름
- 모든 점수를 점수/M*100으로 고침
- 새로운 평균을 구함
'''



# 코드
import sys

sys.stdin = open('input_text/1546.txt')

N = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
new_average = sum(map(lambda score: score / max_score * 100, scores)) / N
print(new_average)


# 실행결과(메모리:31256KB, 시간:44ms)