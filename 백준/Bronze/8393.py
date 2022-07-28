# https://www.acmicpc.net/problem/8393
# 문제8393.합
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 자연수 n
- 1 <= n <= 10,000
'''



# 출력
'''
1. 1부터 n까지의 합을 출력
'''



# 코드
import sys

sys.stdin = open('input_text/8393.txt')

n = int(input())

print(sum(range(1, n + 1)))



# 실행 결과: 성공(메모리:30840kb, 시간:68ms)