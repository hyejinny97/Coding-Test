# https://www.acmicpc.net/problem/9325
# 문제9325번.얼마?
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 테스트 케이스 수 T
2. 자동차의 가격 s
- 1 <= s <= 100,000
3. 구매하려고 하는 서로 다른 옵션의 갯수 n
- 0 <= n <= 1,000
4. n개의 줄에 사려고하는 특정 옵션의 갯수 q, 해당 옵션의 가격 p
- 1 <= q <= 100
- 1 <= p <= 10,000
'''



# 출력
'''
1. 각 테스트 케이스마다, 최종적으로 구매하려는 자동차의 가격 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/9325.txt')

T = int(input())
for _ in range(T):
    tot_price = car_price = int(input())
    option = int(input())
    for _ in range(option):
        num, option_price = map(int, input().split())
        tot_price += option_price * num
    print(tot_price)



# 실행 결과: 성공(메모리:30840kb, 시간:2732ms)