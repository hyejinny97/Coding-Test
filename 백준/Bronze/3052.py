# https://www.acmicpc.net/problem/3052
# 문제3052번.나머지
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 10줄마다 숫자가 주어짐
- 0 <= 숫자 <= 1,000
'''



# 출력
'''
1. 10개의 수를 모두 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력
'''



# 코드
import sys

sys.stdin = open('input_text/3052.txt')

nums = set(int(input()) % 42 for _ in range(10))

print(len(nums))


# 실행결과(메모리:31256KB, 시간:40ms)