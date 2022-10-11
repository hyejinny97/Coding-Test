# https://school.programmers.co.kr/learn/courses/30/lessons/82612
# 코딩테스트연습 < 위클리 체인지 < 문제.부족한 금액 계산하기



# 입력
'''
1. 놀이기구의 원래 이용료 price원, 현재 자신이 가지고 있는 금액 money원, 놀이기구를 탄 횟수 count번
- 1 ≤ price ≤ 2,500
- 1 ≤ money ≤ 1,000,000,000
- 1 ≤ count ≤ 2,500
'''



# 출력
'''
1. 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return
- 금액이 부족하지 않으면 0을 return
- 놀이기구의 원래 이용료는 price원인데, 놀이기구를 N번째 이용한다면 원래 이용료의 N배를 받음
'''



# 코드 1
import sys

sys.stdin = open('input_text/부족한금액계산하기.txt')

def solution(price, money, count):
    # 지불해야하는 총 금액
    tot_price = 0
    for n in range(1, count + 1):
        tot_price += price * n
    
    # 현재 소지한 금액에서 얼마나 모자라는지 반환
    return 0 if money >= tot_price else tot_price - money
        

# 실행 결과: 성공




# 코드 2
import sys

sys.stdin = open('input_text/부족한금액계산하기.txt')

def solution(price, money, count):
    return max(0, price * ((count + 1) * count // 2) - money)


# 실행 결과: 성공