# https://www.acmicpc.net/problem/11021
# 문제11021번.A+B-7
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트케이스 개수 T
2. 정수 A, B
- 0 < A,B < 10
'''



# 출력
'''
1. 'Case #x:'을 출력한 다음, A+B를 출력
'''



# 코드
import sys

T = int(input())

for i in range(1,T+1):
  A, B = map(int, sys.stdin.readline().split())
  print("Case #{}: {}".format(i, A+B))



# 실행결과(메모리:30860KB, 시간:72ms)