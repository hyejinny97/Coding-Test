# https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 코딩테스트연습 < Summer/Winter Coding(~2018) < 문제.예산



# 입력
'''
1. 부서별로 신청한 금액이 들어있는 배열 d
- 1 <= d 길이 <= 100
- 1 <= 금액 <= 100,000
2. 예산 budget
- 1 <= 예산 <= 10,000,000
'''



# 출력
'''
1. 최대 몇 개의 부서에 물품을 지원할 수 있는지 return
- 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼을 모두 지원해 줘야함
'''



# 코드 
import sys

sys.stdin = open('input_text/예산.txt')

def solution(d, budget):
    d.sort()
    pay = 0   # 예산 지출금액
    cnt = 0   # 물품 지원한 총 부서 수
    for money in d:
        if pay + money > budget:
            break
        pay += money
        cnt += 1

    return cnt


# 실행 결과: 성공