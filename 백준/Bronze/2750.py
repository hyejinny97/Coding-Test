# https://www.acmicpc.net/problem/2750
# 문제2750번.수 정렬하기
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 수의 개수 N
- 1 <= N <= 1,000
2. N개의 줄에 정수
- -1,000 <= N <= 1,000
- 수는 중복되지 않음
'''



# 출력
'''
1. N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2750.txt')

N = int(input())

# N개의 수를 입력받아 오름차순 정렬
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()

# 정렬 결과를 출력
print('\n'.join(map(str, nums)))


# 실행 결과: 성공(메모리:31388kb, 시간:96ms)