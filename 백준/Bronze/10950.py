# https://www.acmicpc.net/problem/10950
# 문제10950번.A+B-3
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트케이스 개수 T
2. 정수 A, B
- 0 <= A,B <= 10
'''



# 출력
'''
1. A+B를 출력
'''



# 코드
T = int(input())

for t in range(T):
  A,B = map(int,input().split())
  print(A + B)



# 실행결과(메모리:30864KB, 시간:76ms)