# https://www.acmicpc.net/problem/10989
# 문제10989번.수 정렬하기3
# 시간: 5초, 메모리: 8MB



# 입력
'''
1. 수의 개수 N
- 1 ≤ N ≤ 10,000,000
2. N개의 줄에 자연수
- 0 < 자연수 ≤ 10,000
'''



# 출력
'''
1. N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/10989.txt')

N = int(input())

# N개의 정수를 입력받아 오름차순 정렬
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

# 정렬된 결과를 출력
for n in nums:
    print(n)


# 실행 결과: 실패(메모리 초과)



# 코드 2
import sys

sys.stdin = open('input_text/10989.txt')

N = int(input())

# N개의 정수를 입력받기
nums = [0] * 10001   # idx: 0 ~ 10,000까지 수, value: 개수
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

# 정렬된 결과를 출력
for i in range(1, 10000 + 1):
    print(f'{i}\n' * nums[i], end='')


# 실행 결과: 실패(메모리 초과)



# 코드 3
import sys

sys.stdin = open('input_text/10989.txt')

N = int(input())

# N개의 정수를 입력받기
nums = [0] * 10001   # idx: 0 ~ 10,000까지 수, value: 개수
for _ in range(N):
    nums[int(sys.stdin.readline())] += 1

# 정렬된 결과를 출력
for i in range(1, 10000 + 1):
    for _ in range(nums[i]):
        print(i)


# 실행 결과: 성공(메모리:31256kb, 시간:8868ms)