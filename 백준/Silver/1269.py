# https://www.acmicpc.net/problem/1269
# 문제1269번.대칭 차집합
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 집합 A의 원소의 개수, 집합 B의 원소의 개수
2. 집합 A의 모든 원소
3. 집합 B의 모든 원소
- 0 < 집합의 원소의 개수 <= 200,000
- 0 < 원소 <= 100,000,000
'''



# 출력
'''
1. 대칭 차집합의 원소의 개수를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/1269.txt')

A, B = map(int, input().split())
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))

print(len(set_A ^ set_B))


# 실행 결과: 성공(메모리:88612kb, 시간:248ms)