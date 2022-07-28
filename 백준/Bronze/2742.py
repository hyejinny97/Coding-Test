# https://www.acmicpc.net/problem/2742
# 문제2742.기찍 N
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 자연수 n
- 0 < n <= 100,000
'''



# 출력
'''
1. n부터 1까지 한 줄에 하나씩 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2742.txt')

n = int(input())

for i in range(n, 1 - 1, -1):
    print(i)



# 실행 결과: 성공(메모리:30840kb, 시간:112ms)