# https://www.acmicpc.net/problem/15439
# 문제15439번.베라의 패션
# 시간: 2초, 메모리: 256MB



# 입력
'''
1. 상의 N 벌과 하의 N 벌
- 1 ≤ N ≤ 2017
- i 번째 상의와 i 번째 하의는 모두 색상 i를 가짐
'''



# 출력
'''
1. 상의와 하의가 서로 다른 색상인 조합의 가짓수를 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/15439.txt')

def combination(N, M) -> int:   # nPm
    if N < M:
        return 0
    
    rst = 1
    for n in range(N, N - M, -1):  
        rst *= n

    return rst


N = int(input())

print(combination(N, 2))


# 실행 결과: 성공(메모리:31256kb, 시간:60ms)

