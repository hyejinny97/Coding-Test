# https://www.acmicpc.net/problem/2739
# 문제2739.구구단
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 구구단 N
- 1 <= N <= 9
'''



# 출력
'''
1. 각 줄에 N * 1부터 N * 9까지 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2739.txt')

dan = int(input())

for n in range(1, 9 + 1):
    print(f'{dan} * {n} = {dan * n}')



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)