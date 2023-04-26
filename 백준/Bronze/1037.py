# https://www.acmicpc.net/problem/1037
# 문제1037번.약수
# 시간: 2초, 메모리: 512MB



# 입력
'''
1. N의 진짜 약수의 개수
- 0 < 약수의 개수 <= 50
2. N의 진짜 약수
- 2 <= 약수 <= 1,000,000
- 중복되지 않음
'''



# 출력
'''
1. N을 출력
- 양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 함
'''



# 코드 

# 접근방법
'''
N = 약수들 중 최솟값 x 최댓값
'''
import sys

sys.stdin = open('input_text/1010.txt')

N = int(input())
nums = list(map(int, input().split()))
print(min(nums) * max(nums))


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)

