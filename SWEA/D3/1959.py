# 문제1959번.두 개의 숫자열
# 시간: 30초, 메모리: 256MB



# 입력
'''
1. 테스트 케이스 T
2. 배열 A의 갯수 N, 배영열 B의 갯수 M
- 3 <= N, M <= 20
3. 배열 A
4. 배열 B
'''



# 출력
'''
1. #{테스트케이스} {서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값}
'''



# 코드
import sys

sys.stdin = open('../input_text/1959.txt')

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 두 배열 중 더 긴 배열 찾기
    long = A if len(A) > len(B) else B   # 더 긴 배열
    short = B if len(A) > len(B) else A   # 더 짧은 배열

    # 긴 배열을 순회하면서 짧은 배열의 값과 곱하기
    max_mul_sum = 0
    for start in range(0, max(N, M) - min(N, M) + 1):
        long_piece = long[start:start + min(N, M)]
        mul_sum = 0   # 곱하고 더한 값
        for i in range(min(N, M)):
            mul_sum += long_piece[i] * short[i]
        max_mul_sum = max(max_mul_sum, mul_sum)
    
    print(f'#{test_case} {max_mul_sum}')



# 실행 결과: 성공(메모리:56,668 kb, 시간:140 ms)