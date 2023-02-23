# https://www.acmicpc.net/problem/1427
# 문제1427번.소트인사이드
# 시간: 2초, 메모리: 128MB



# 입력
'''
1. 자연수 N
- 0 < N <= 1,000,000,000
'''



# 출력
'''
1. N의 각 자리수를 내림차순으로 정렬한 후 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/1427.txt')

# N을 입력받고 내림차순으로 정렬
N = list(input())
N.sort(reverse=True)

# 내림차순으로 정렬한 수를 출력
print(''.join(N))


# 실행 결과: 성공(메모리:31256kb, 시간:40ms)
