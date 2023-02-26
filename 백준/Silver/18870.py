# https://www.acmicpc.net/problem/18870
# 문제18870번.좌표 압축
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. 수직선 위의 좌표 개수 N
- 1 ≤ N ≤ 1,000,000
2. N개의 좌표 X
- -10^9 ≤ X ≤ 10^9
'''



# 출력
'''
1. N개의 각 좌표를 압축한 결과를 공백으로 구분해서 출력

<좌표 압축>
압축한 결과 = 좌표 X보다 값이 작은 좌표의 개수
'''



# 코드 

# 접근방법
'''
좌표    -10  -9  2  4
                    4

정렬순서  0   1  2  3
압축결과  0   1  2  3

압축한 결과 = 좌표 X보다 작은 좌표의 개수
            = 정렬 순서
'''

import sys

sys.stdin = open('input_text/18870.txt')

# N개의 좌표를 받아 중복 없애기
N = int(input())
nums = list(map(int, input().split()))
nums_set = set(nums)

# 중복 제거한 좌표들 정렬 후, 딕셔너리화 하기(key:좌표, value:압축결과)
nums_order = sorted(nums_set)
nums_dict = {}
for i in range(len(nums_order)):
    nums_dict[nums_order[i]] = i

# N개 좌표의 각 압축결과 출력
for num in nums:
    print(nums_dict[num], end=" ")


# 실행 결과: 성공(메모리:171168kb, 시간:1984ms)
