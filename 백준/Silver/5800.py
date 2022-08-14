# https://www.acmicpc.net/problem/5800
# 문제5800번.성적 통계
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 반의 수 K
- 1 <= K <= 100
2. K개의 줄에 각 반의 학생 수 N, N명의 각 수학 성적
- 2 <= N <= 50
- 0 <= 성적 <= 100
'''



# 출력
'''
1. Class {반 번호}
2. 가장 높은 점수, 가장 낮은 점수, 성적을 내림차순으로 정렬했을때 가장 큰 인접한 점수 차이 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/5800.txt')

T = int(input())
for test_case in range(1, T + 1):
    row = list(map(int, input().split()))
    n, scores = row[0], row[1:]
    scores.sort(reverse=True)   # 내림차순 정렬
    
    max_gap = 0   # 가장 큰 인접한 점수 차
    for i in range(0, n - 1):
        gap = scores[i] - scores[i + 1]
        if gap > max_gap:
            max_gap = gap
    
    print(f'Class {test_case}')
    print(f'Max {scores[0]}, Min {scores[-1]}, Largest gap {max_gap}')




# 실행 결과: 성공(메모리:30840kb, 시간:84ms)