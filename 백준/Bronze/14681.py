# https://www.acmicpc.net/problem/14681
# 문제14681.사분면 고르기
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 정수 x
- -1,000 <= x, y <= 1,000 (0은 아님)
'''



# 출력
'''
1. 점 (x, y)의 사분면 번호(1/2/3/4)를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2753.txt')

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)