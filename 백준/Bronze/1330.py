# https://www.acmicpc.net/problem/1330
# 문제1330.두 수 비교하기
# 시간: 1초, 메모리: 512MB



# 입력
'''
1. 정수 A, B
- -10,000 <= A, B <= 10,000
'''



# 출력
'''
1. A와 B 크기를 비교 
- A > B이면, '>' 출력
- A < B이면, '<' 출력
- A == B이면, '==' 출력
'''



# 코드
import sys

sys.stdin = open('input_text/1330.txt')

A, B = map(int, input().split())

if A == B:
    print('==')
elif A > B:
    print('>')
else:
    print('<')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)