# 문제2063.중간값 찾기
# 시간: 30초, 메모리: 256MB

# 입력
'''
1. 점수 갯수 N
2. N개의 각 점수
- 9 <= 점수 <= 199
- N은 항상 홀수로 주어짐
'''

# 출력
'''
N개의 점수 중 중간값을 출력
'''

# 코드
import sys

sys.stdin = open('SWEA/input_text/2063.txt', 'r')

N = int(input())
scores = list(map(int, input().split()))
scores.sort()
print(scores[N//2])

# 실행 결과: 성공(메모리:57,200 kb, 시간:129 ms)