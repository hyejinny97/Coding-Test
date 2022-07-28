# https://www.acmicpc.net/problem/2741
# 문제2741.N 찍기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 자연수 n
- 0 < n <= 100,000
'''



# 출력
'''
1. 1부터 n까지 한 줄에 하나씩 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2741.txt')

n = int(input())

for i in range(1, n + 1):
    print(i)



# 실행 결과: 성공(메모리:30840kb, 시간:112ms)