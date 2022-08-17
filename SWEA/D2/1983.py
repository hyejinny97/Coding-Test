# 문제1983번.조교의 성적 매기기
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트케이스 갯수 T
2. 학생 수 N, 학점을 알고 싶은 학생의 번호 K
- 10 <= N <= 100
- N은 10의 배수
- 1 <= K <= N
- K번쨰 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않음
3. N개의 줄에 각각의 학생이 받은 시험 및 과제 점수
'''



# 출력
'''
1. #{테스트케이스} {K번째 학생의 학점}
- 총 10개의 평점
- 중간,기말,과제 점수가 서로 다른 비율로 점수에 반영됨
- 10개의 평점을 각각 같은 비율로 부여
'''



# 코드 
from ast import Lambda
import sys

sys.stdin = open('../input_text/1983.txt', 'r')

# 평점
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    
    # 학생 N명 각각의 총점 구하기
    scores = []   # 인덱스: 학생 0번 ~ (N-1)번, 값: (번호, 총점)
    for num in range(N):
        mid, final, assignment = map(int, input().split())
        score = mid * 0.35 + final * 0.45 + assignment * 0.2
        scores.append((num, score))

    # 총점이 높은 순서대로 줄세우기
    scores.sort(key=lambda x: x[1], reverse=True)

    # K번째 학생의 등수 찾기
    rate = 0
    for i in range(N):
        if scores[i][0] == K - 1:
            rate = i
            break
    
    # K번째 학생의 학점 출력
    print(f'#{test_case} {grades[rate // (N // 10)]}')



# 실행 결과: 성공(메모리:57,196 kb, 시간:166 ms)