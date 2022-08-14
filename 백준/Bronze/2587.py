# https://www.acmicpc.net/problem/2587
# 문제2587번.대표값2
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 5개의 줄에 각각 자연수
- 0 < 자연수 < 100
- 10의 배수
'''



# 출력
'''
1. 평균 출력
2. 중앙값 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2587.txt')

nums = [int(input()) for _ in range(5)]

print(sum(nums) // 5)
print(sorted(nums)[2])



# 실행 결과: 성공(메모리:30840kb, 시간:72ms)