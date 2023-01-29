# https://www.acmicpc.net/problem/18108
# 문제18108번.1998년생인 내가 태국에서는 2541년생?!
# 시간: 1초, 메모리: 1024MB



# 입력
'''
1. 불기 연도 y
- 1,000 <= y <= 3,000
'''



# 출력
'''
1. 불기 연도를 서기 연도로 변환한 결과를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/18108.txt')

y = int(input())
print(y - 543)


# 실행 결과: 성공(메모리:30864kb, 시간:68ms)