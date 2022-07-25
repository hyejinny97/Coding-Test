# https://www.acmicpc.net/problem/8958
# 문제8958번.OX퀴즈
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 테스트케이스 개수 T
2. OX문자열
- 0 <= 문자열 길이 <= 80
'''



# 출력
'''
1. 현재 문제까지 연속된 O의 갯수를 구한 후, 다 더해 점수를 출력
'''



# 코드
import sys

sys.stdin = open("input_text/3_OX퀴즈.txt")

T = int(input())
for _ in range(T):
    quizs = input()
    rst = 0   # 총 점수
    score = 0   # 현재 점수
    # OX문자열을 for 반복문으로 하나씩 읽어가면서 연속된 O의 갯수 카운트한 후 합하기
    for quiz in quizs:
        # 퀴즈 결과가 'X'인 경우
        if quiz != 'O':
            score = 0   # 0으로 초기화
            continue
        # 퀴즈 결과가 'O'인 경우
        score += 1
        rst += score
        
    print(rst)



# 실행결과(메모리:30840KB, 시간:92ms)