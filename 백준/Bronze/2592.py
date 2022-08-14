# https://www.acmicpc.net/problem/2592
# 문제2592번.대표값
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 10개의 줄에 각각 자연수 하나
- 0 < 자연수 < 1,000
- 10의 배수
'''



# 출력
'''
1. 평균 출력
2. 최빈값 출력
- 최빈값이 둘 이상일 경우, 하나만 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2592.txt')

nums = {}   # 키: 10 ~ 1000까지 10의 배수, 값: 각 자연수의 갯수

# 평균 출력
sum_nums = 0
for _ in range(10):
    num = int(input())
    sum_nums += num
    if nums.get(num):
        nums[num] += 1
    else:
        nums[num] = 1

print(sum_nums // 10)

# 최빈값 출력
print(max(nums, key=lambda x: nums[x]))



# 실행 결과: 성공(메모리:30840kb, 시간:80ms)