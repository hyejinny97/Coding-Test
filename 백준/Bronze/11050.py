# https://www.acmicpc.net/problem/11050
# 문제11050번.이항계수1
# 시간: 1초, 메모리: 256MB



# 입력
'''
1. 자연수 N, 정수 K
- 1 <= N <= 10
- 0 <= K <= N
'''



# 출력
'''
1. N, K의 이항계수 출력
'''



# 코드 
import sys

sys.stdin = open('input_text/11050.txt')

def combination(N, K):
    if K == 0:
        return 1
    
    K = min(K, N - K)
    rst = 1
    
    for n in range(N, N - K, -1):  # 분자
        rst *= n
    for k in range(K, 0, -1):   # 분모
        rst //= k
    
    return rst

N, K = map(int, input().split())
print(combination(N, K))


# 실행 결과: 성공(메모리:31256kb, 시간:56ms)

