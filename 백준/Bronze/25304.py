# https://www.acmicpc.net/problem/25304
# 문제25304번.영수증
# 시간: 1초, 메모리: 1024MB



# 입력
'''
1. 영수증에 적힌 총 금액 X
- 1 <= X <= 1,000,000,000
2. 구매한 물건의 종류 수 N
- 1 <= N <= 100
3. N개의 줄에 각 물건의 가격 a와 개수 b
- 1 <= a <= 1,000,000
- 1 <= b <= 10
'''



# 출력
'''
1. 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes 출력, 일치하지 않는다면 No 출력
'''



# 코드
import sys

sys.stdin = open('input_text/25304.txt')

tot_price = int(input())
N = int(input())

sum_price = 0
for _ in range(N):
    price, num = map(int, input().split())
    sum_price += price * num

# 총 금액이 일치한지 확인
if sum_price == tot_price:
    print('Yes')
else:
    print('No')



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)