# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# 코딩테스트연습 < 월간 코드 챌린지 시즌2 < 문제.음양 더하기



# 입력
'''
1. 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes
- 1 <= absolutes 길이 <= 1,000
- 1 <= 정수 <= 1,000
2. 정수들의 부호를 차례대로 담은 불리언 배열 signs
- signs 길이 = absolutes 길이
- signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수, 그렇지 않으면 음수
'''



# 출력
'''
1. 실제 정수들의 합을 구하여 return 
'''



# 코드
import sys

sys.stdin = open('input_text/음양더하기.txt')

def solution(absolutes, signs):
    sum_nums = 0
    for i in range(len(absolutes)):
        if signs[i]:
            sum_nums += absolutes[i]
        else:
            sum_nums += -absolutes[i]
    return sum_nums
        

# 실행 결과: 성공