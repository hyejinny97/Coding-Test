# https://www.acmicpc.net/problem/2108
# 문제2108번.통계학
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 수의 개수 N
- 1 ≤ N ≤ 500,000
- N은 홀수
2. N개의 줄에 정수
- -4,000 ≤ 정수 ≤ 4,000
'''



# 출력
'''
1. 산술평균을 출력
- 산술평균 : N개의 수들의 합을 N으로 나눈 값
- 소수점 이하 첫째 자리에서 반올림한 값을 출력
2. 중앙값을 출력
- 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
3. 최빈값을 출력
- 최빈값 : N개의 수들 중 가장 많이 나타나는 값
- 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력
4. 범위를 출력
- 범위 : N개의 수들 중 최댓값과 최솟값의 차이
'''



# 코드 
import sys
from collections import Counter

sys.stdin = open('input_text/2108.txt')

N = int(input())

# N개의 정수를 입력받아 오름차순 정렬
nums = [int(sys.stdin.readline()) for _ in range(N)]
nums.sort()

# 산술평균
print(round(sum(nums)/len(nums)))

# 중앙값
print(nums[len(nums) // 2])

# 최빈값
cnt_of_nums = Counter(nums)   # key: -4,000 ~ 4,000 정수, value: 정수 개수
max_value = 0    # 최빈값(value)
elements = []    # 최빈값인 요소(key)
for num in cnt_of_nums:
    if cnt_of_nums[num] > max_value:
        max_value = cnt_of_nums[num]
        elements = [num]
    elif cnt_of_nums[num] == max_value:
        elements.append(num)

if len(elements) >= 2:
    print(sorted(elements)[1])
else:
    print(elements[0])

# 범위
print(max(nums) - min(nums))


# 실행 결과: 성공(메모리:53736kb, 시간:476ms)
