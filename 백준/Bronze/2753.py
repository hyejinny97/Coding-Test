# https://www.acmicpc.net/problem/2753
# 문제2753.윤년
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 연도
- 1 <= 연도 <= 4,000
'''



# 출력
'''
1. 윤년이면 1, 아니면 0 출력
- 윤년: 4의 배수 and (100의 배수가 아님 or 400의 배수)
'''



# 코드
import sys

sys.stdin = open('input_text/2753.txt')

year = int(input())

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(1)
else:
    print(0)


# 실행 결과: 성공(메모리:30840kb, 시간:80ms)