# https://www.acmicpc.net/problem/11022
# 문제11022번.A+B-8
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트케이스 개수 T
2. 정수 A, B
- 0 < A,B < 10
'''



# 출력
'''
1. 'Case #x: A + B = C' 형식으로 출력
'''



# 코드
import sys

T = int(input())

for i in range(1, T+1):
  A, B = map(int, sys.stdin.readline().split())
  print("Case #{0}: {1} + {2} = {3}".format(i, A, B, A+B))



# 실행결과(메모리:30840KB, 시간:68ms)