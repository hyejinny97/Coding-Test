# https://www.acmicpc.net/problem/2979
# 문제2979번.트럭주차
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 주차요금 A, B, C
- 트럭 한 대를 주차할 경우, 1분에 1대당 A원을 냄
- 트럭 두 대를 주차할 경우, 1분에 1대당 B원을 냄
- 트럭 세 대를 주차할 경우, 1분에 1대당 C원을 냄
- 1 <= C <= B <= A <= 100
2. 3개의 줄에 트럭이 주차장에 도착한 시간, 떠난 시간
- 1 < 시간 < 100
'''



# 출력
'''
1. 내야 하는 주차 요금 출력
- 주차하는 트럭의 수에 따라서 주차 요금을 할인해줌
'''



# 코드 1 
import sys

sys.stdin = open('input_text/2979.txt')

A, B, C = map(int, input().split())

# 주차한 트럭 갯수에 따른 주차요금
price = {   
    1: A,
    2: B,
    3: C
}

# 분당 주차된 트럭 갯수
cnt_per_minute = [0] * 101   # 1분 ~ 100분
for _ in range(3):
    depature, arrival = map(int, input().split())
    
    for i in range(depature + 1, arrival + 1):
        cnt_per_minute[i] += 1

# 분당 요금 = 1분에 1대당 요금 x 차 갯수
tot_price = 0
for i in range(1, 100 + 1):
    price_per_minute = price.get(cnt_per_minute[i], 0) * cnt_per_minute[i]
    tot_price += price_per_minute

print(tot_price)



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)



# 코드 2
import sys
from collections import Counter

sys.stdin = open('input_text/2979.txt')

A, B, C = map(int, input().split())

# 주차한 트럭 갯수에 따른 주차요금
price = {   
    1: A,
    2: B,
    3: C
}

# 분당 주차된 트럭 갯수
cnt_per_minute = [0] * 101   # 1분 ~ 100분
for _ in range(3):
    depature, arrival = map(int, input().split())
    
    for i in range(depature + 1, arrival + 1):
        cnt_per_minute[i] += 1

# 총 요금 = (1분에 1대당 요금 x 차 갯수 x 시간(분))의 합
cnt_minute = Counter(cnt_per_minute)   # 키: 차 갯수, 값: 시간

tot_price = price[1] * 1 * cnt_minute[1] + price[2] * 2 * cnt_minute[2] + price[3] * 3 * cnt_minute[3]

print(tot_price)



# 실행 결과: 성공(메모리:32432kb, 시간:84ms)