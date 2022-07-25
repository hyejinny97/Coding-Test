# https://www.acmicpc.net/problem/10953
# 문제10953번.A+B-6
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 테스트케이스 개수 T
2. 정수 A, B가 콤마로 구분되어서 입력됨
- 0 <= A,B <= 10
'''



# 출력
'''
1. A+B를 출력
'''



# 코드
T = int(input())
for _ in range(T):
    a, b = map(int, input().split(','))
    print(a + b)



# 실행결과(메모리:30840KB, 시간:76ms)