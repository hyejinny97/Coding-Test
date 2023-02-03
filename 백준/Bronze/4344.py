# https://www.acmicpc.net/problem/4344
# 문제4344번.평균은 넘겠지
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트 케이스의 개수 T
2. T개 줄에 학생의 수 N, N명의 점수
- 1 ≤ N ≤ 1,000
- 0 <= 점수 <= 100
'''



# 출력
'''
1. 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력
'''



# 코드
import sys

sys.stdin = open("input_text/4344.txt")

T = int(input())
for _ in range(T):
    line = list(map(int, input().split()))
    N, scores = line[0], line[1:]
    avg = sum(scores) / N
    over_avg = list(filter(lambda score: score > avg, scores))  # 평균 넘는 학생들
    print(f'{(len(over_avg) / N * 100):.3f}%')


# 실행결과(메모리:31256KB, 시간:48ms)