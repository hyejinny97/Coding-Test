# https://www.acmicpc.net/problem/3046
# 문제3046번.R2
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 두 정수 R1, S
- -1,000 <= R1, S <= 1,000
'''



# 출력
'''
1. R2를 출력
- S = (R1 + R2) / 2
'''



# 코드
import sys

sys.stdin = open('input_text/3046.txt')

R1, S = map(int, input().split())
R2 = S * 2 - R1
print(R2)



# 실행결과(메모리:30840KB, 시간:76ms)