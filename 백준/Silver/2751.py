# https://www.acmicpc.net/problem/2751
# 문제2751번.수 정렬하기2
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 수의 개수 N
- 1 ≤ N ≤ 1,000,000
2. N개의 줄에 정수
- -1,000,000 ≤ 정수 ≤ 1,000,000
- 수는 중복되지 않음
'''



# 출력
'''
1. N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2751.txt')

N = int(input())

# N개의 정수를 입력받아 오름차순 정렬
nums = [int(input()) for _ in range(N)]
nums.sort()

# 정렬된 결과를 출력
for n in nums:
    print(n)


# 실행 결과: 실패(시간초과)



# 코드 2
import sys

sys.stdin = open('input_text/2751.txt')

N = int(input())

# N개의 정수를 입력받아 오름차순 정렬
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

# 정렬된 결과를 출력
for n in nums:
    print(n)


# 실행 결과: 성공(메모리:77108kb, 시간:1392ms)