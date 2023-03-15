# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 코딩테스트연습 < 스택/큐 < 문제.주식가격



# 입력
'''
1. 초 단위로 기록된 주식가격이 담긴 배열 prices
- 1 <= 가격 <= 10,000
- 2 <= prices 길이 <= 100,000
'''



# 출력
'''
1. 가격이 떨어지지 않은 기간은 몇 초인지를 return
'''


# 코드 
import sys

sys.stdin = open('input_text/주식가격.txt')

def solution(prices):
    times = [0] * len(prices)   # 각 주식 가격이 떨어지지 않은 기간
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            times[i] += 1
            if prices[i] > prices[j]:
                break
       
    return times


# 실행 결과: 성공