# 문제4466번.최대 성적표 만들기
# 시간: 4초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 총 과목 수 N개, 선택할 수 있는 과목 수 K개
- 1 <= K <= N <= 100
3. N개 과목의 각 점수
- 0 <= 점수 <= 100
'''



# 출력
'''
1. #{테스트케이스} {성적표에 표시될 총점의 최댓값}
'''



# 코드 1
import sys
from itertools import combinations

sys.stdin = open('../input_text/4466.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    # N개의 과목 중 K개를 선택
    choices = combinations(scores, K)
    
    # K개 과목의 총점들 중 최댓값 찾기
    max_score = 0
    for choice in choices:
        max_score = max(max_score, sum(choice))
    
    print(f'#{test_case} {max_score}')



# 실행 결과: 실패(제한시간 초과, 100개 중 0개 통과)



# 코드 2
import sys

sys.stdin = open('../input_text/4466.txt')

# N개의 과목 중에서 K개 선택해서 합치기
def choiceK(start, K, choices):
    global max_score
    
    # K개 모두 선택한 경우
    if K <= 0:
        max_score = max(max_score, sum(choices))
        return
    
    # 과목 선택하기
    for i in range(start, len(scores)):
        choiceK(i + 1, K - 1, choices + [scores[i]])


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # N개의 과목 중 K개를 선택해 더한 총점 중 최댓값 찾기
    max_score = 0
    choiceK(0, K, [])

    print(f'#{test_case} {max_score}')



# 실행 결과: 실패(제한시간 초과, 100개 중 0개 통과)



# 코드 3
import sys

sys.stdin = open('../input_text/4466.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    
    # N개의 과목을 내림차순으로 정렬
    scores.sort(reverse=True)

    # 상위 성적 K개만큼 선택해서 합하기
    max_score = sum(scores[:K])

    print(f'#{test_case} {max_score}')



# 실행 결과: 성공(메모리:59,864 kb , 시간:145 ms)