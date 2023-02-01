# https://www.acmicpc.net/problem/2562
# 문제2562번.최댓값
# 시간: 1초, 메모리: 128MB



# 입력
'''
1. 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어짐
- 0 < 자연수 <= 100
'''



# 출력
'''
1. 최댓값을 출력
2. 최댓값이 몇 번째 수인지를 출력
'''



# 코드
import sys

sys.stdin = open('input_text/2562.txt')

nums = [[i, int(input())] for i in range(1, 9 + 1)]

max_num = max(nums, key=lambda num: num[1])
print(max_num[1], max_num[0], sep='\n')


# 실행 결과: 성공(메모리:31256kb, 시간:44ms)