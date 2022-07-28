# https://www.acmicpc.net/problem/10950
# 문제10952번.A+B-5
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 정수 A, B
- 0 <= A,B <= 10
- 입력 마지막에는 0이 입력됨
'''



# 출력
'''
1. 각 줄마다 A+B를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/10952.txt')

while True:
  A,B = map(int,input().split())
  if A == 0 and B == 0:
    break
  print(A + B)



# 실행 결과: 성공(메모리:30840kb, 시간:76ms)